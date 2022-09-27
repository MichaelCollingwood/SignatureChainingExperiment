import json


class SerialisableObject:
    """Class allowing Message and SignedMessage to dumped to JSON"""

    def to_json(self) -> str:
        """Convert a custom object to a JSON object"""

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
