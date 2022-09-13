import json
import os

from message import SignedMessage


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
