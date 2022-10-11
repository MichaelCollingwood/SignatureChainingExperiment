import json
import os
from hashlib import sha256
from typing import List

from encryption import RSAAlgorithm, get_public_key
from messages import Message, SignedMessage, ReceivedMessage


class Sender:
    """Signs then sends or shares messages"""

    def __init__(self, sender_id):
        self.id = sender_id

        self.rsaAlgorithm = RSAAlgorithm(512)
        self.rsaAlgorithm.publish(sender_id)

    def send(self, queue_address: str, message: Message) -> None:
        """Posts message to a queue"""

        Queue(queue_address).append(
            self.sign(message)
        )

    def share(self, queue_address: str, signed_message: SignedMessage) -> None:
        """Shares signed_message to a queue, adding this sender as an additional source"""

        Queue(queue_address).append(
            self.sign(
                message=signed_message.message.make_shareable(self.id),
                encrypted_hashes=signed_message.encrypted_hashes
            )
        )

    def sign(self, message: Message, encrypted_hashes: List[int] = None) -> SignedMessage:
        """Encrypt a hash of the message to send with the message in SignedMessage"""

        encoded_message = message.to_json().encode()
        hash_ = int(sha256(encoded_message).hexdigest(), 16)
        encrypted_hash = self.rsaAlgorithm.encrypt(hash_)

        return SignedMessage(message, (encrypted_hashes or []) + [encrypted_hash])


class Queue:
    """Represents a queue. Each entry is a dictionary held in a list"""

    def __init__(self, queue_address):
        self.queue_address = queue_address

        if os.path.exists(self.queue_address) and os.path.getsize(self.queue_address) > 0:
            with open(self.queue_address, 'r') as f:
                self.entries = json.load(f)
        else:
            with open(self.queue_address, 'w'):
                self.entries = []

    def consume(self) -> SignedMessage | None:
        """Take the top entry and update the queue"""

        if len(self.entries) > 0:
            entry = self.entries.pop(0)
            self.update()

            return SignedMessage.from_json(entry)

    def append(self, entry) -> None:
        """Add entry to the bottom and update the queue"""

        self.entries.append(entry)
        self.update()

    def update(self) -> None:
        """Write the queue to JSON file"""

        with open(self.queue_address, 'w') as f:
            f.write(self.to_json())

    def to_json(self) -> str:
        """Convert queue to a JSON"""

        entries_json = [dict(signed_message) for signed_message in self.entries]

        return json.dumps(entries_json, indent=4)


class Consumer:
    """Consumes and checks messages taken off a queue"""

    def __init__(self):
        self.received_messages: List[ReceivedMessage] = []

    def consume(self, queue_address) -> None:
        """Take message off a queue and authenticate it"""

        signed_message = Queue(queue_address).consume()
        if signed_message is not None:
            authentic = self.authenticate(
                signed_message.message,
                signed_message.encrypted_hashes
            )

            received_message = ReceivedMessage(signed_message, authentic)

            received_message.display_received_message()
            self.received_messages.append(received_message)
        else:
            print("Cannot consume from empty queue.\n")

    @staticmethod
    def authenticate(message: Message, encrypted_hashes: List[int]) -> List[bool]:
        """For each source, verify encrypted hash correct using public key"""

        n_sources = len(message.sources)
        authentic = [False] * n_sources

        for i, [source, encrypted_hash] in enumerate(list(zip(message.sources, encrypted_hashes))[::-1]):
            message_ = message.copy(
                sources=message.sources[:n_sources-i],
                timestamps=message.timestamps[:n_sources-i]
            )  # Message at time of encryption

            encoded_message = message_.to_json().encode()
            hash_ = int(sha256(encoded_message).hexdigest(), 16)

            decrypted_hash = pow(encrypted_hash, *get_public_key(source))

            authentic[i] = hash_ == decrypted_hash

        return authentic
