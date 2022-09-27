import sys

from Image import DecodedImage
from message import Message
from consumer import Consumer
from sender import Sender


class User(Sender, Consumer):
    """Implementation of code to send, read and share messages in a loop"""

    def __init__(self, sender_id):
        Sender.__init__(self, sender_id)
        Consumer.__init__(self)

    def run(self) -> None:
        """Manually trigger actions in a while loop as a user"""

        while True:
            command = input(
                '\nSend, consume or share last message?\n'
                '(\'s,<queue>,<type: txt/img>,<content>\'/\'c,<queue>\'/\'sh,<queue>\'):\n'
            ).split(',')

            {
                's': self.send_to_queue,
                'c': self.consume,
                'sh': lambda q: self.share(q, self.received_messages[-1].signed_message),
            }[command[0]](*command[1:])

    def send_to_queue(self, queue, content_type, content) -> None:
        """Given text or an image file, send data to the queue"""

        data = {
            'txt': lambda c: c,
            'img': lambda c: DecodedImage(file=c).decoded_bytes
        }[content_type](content)

        self.send(queue, Message(data, content_type, [self.id]))


user = User(sys.argv[1])
user.run()
