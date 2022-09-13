from hashlib import sha256
from typing import List, Tuple

from Image import DecodedImage
from message import Message, ReceivedMessage
from queue import Queue


def get_public_key(source) -> Tuple[int, int]:
    """Get public key related to a source"""

    with open(f'public_keys/{source}_public_key.csv', 'r') as f:
        key_public, space = f.read().split(',')
        return int(key_public), int(space)


def display_received_message(received_message: ReceivedMessage) -> None:
    """Print or plot message data and describe sources"""

    message = received_message.signed_message.message
    authentic = received_message.authentic

    {
        'txt': lambda d: print(f"\nMessage text:\n\'{d}\'"),
        'img': lambda d: DecodedImage.display(decoded_bytes=d)
    }[message.content_type](message.data)

    print(
        "\nMessage sources:\n" + '\n'.join(
            [f"{s} ===>\t {'Authentic' if a else 'Not Authentic'}" for s, a in zip(message.sources, authentic)]
        ) + '\n'
    )


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

            display_received_message(received_message)
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
