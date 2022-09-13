from hashlib import sha256
from typing import List

from message import Message, SignedMessage
from queue import Queue
from encryption import RSAAlgorithm


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
        """Encrypt a hash of the message to send with the message in SignedMessagev"""

        encoded_message = message.to_json().encode()
        hash_ = int(sha256(encoded_message).hexdigest(), 16)
        encrypted_hash = self.rsaAlgorithm.encrypt(hash_)

        return SignedMessage(message, (encrypted_hashes or []) + [encrypted_hash])
