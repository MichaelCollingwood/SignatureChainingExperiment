import copy
from datetime import datetime
from typing import List

from utilClasses.decodedImage import DecodedImage
from utilClasses.serialisableObject import SerialisableObject


class Message(SerialisableObject):
    """Wrapped data inc. sources and other headers"""

    def __init__(self, data: str, content_type: str, sources: List[str], timestamps=None):
        self.data = data
        self.content_type = content_type
        self.sources = sources
        self.timestamps = timestamps or [datetime.now().strftime("%Y/%m/%d %H:%M:%S")]

    def make_shareable(self, sharer: str):
        """Add sources (and timestamps) to wrapped data for sharing"""

        self.sources.append(sharer)
        self.timestamps.append(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        return self

    def copy(self, **attributes):
        """Copy Message with certain attributes changed"""

        message_copy = copy.deepcopy(self)
        for attr, value in attributes.items():
            message_copy.__setattr__(attr, value)

        return message_copy


class SignedMessage(SerialisableObject):
    """Wrapper for Message with encrypted hashes"""

    def __init__(self, message: Message, encrypted_hashes: List[int]):
        self.message = message
        self.encrypted_hashes = encrypted_hashes

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value.__dict__ if isinstance(value, Message) else value

    @staticmethod
    def from_json(json_dct):
        """Create a signed message from a JSON object"""

        return SignedMessage(
            message=Message(
                data=json_dct['message']['data'],
                content_type=json_dct['message']['content_type'],
                sources=json_dct['message']['sources'],
                timestamps=json_dct['message']['timestamps']
            ),
            encrypted_hashes=json_dct['encrypted_hashes']
        )


class ReceivedMessage:
    """Wrapper for Message with source authenticities"""

    def __init__(self, signed_message: SignedMessage, authentic: List[bool]):
        self.signed_message: SignedMessage = signed_message
        self.authentic: List[bool] = authentic

    def display_received_message(self) -> None:
        """Print or plot message data and describe sources"""

        message = self.signed_message.message
        authentic = self.authentic

        {
            'txt': lambda d: print(f"\nMessage text:\n\'{d}\'"),
            'img': lambda d: DecodedImage.display(decoded_bytes=d)
        }[message.content_type](message.data)

        print(
            "\nMessage sources:\n" + '\n'.join(
                [f"{s} ===>\t {'Authentic' if a else 'Not Authentic'}" for s, a in zip(message.sources, authentic)]
            ) + '\n'
        )
