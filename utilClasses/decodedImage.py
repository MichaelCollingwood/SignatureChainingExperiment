import base64
from io import BytesIO
from PIL import Image


class DecodedImage:
    """Wrapper for decoded image bytes"""

    def __init__(self, file):
        with open(file, "rb") as f:
            self.decoded_bytes = base64.b64encode(f.read()).decode()

    @staticmethod
    def display(decoded_bytes) -> None:
        """Display image represented in decoded_bytes"""

        file_like = BytesIO(base64.b64decode(decoded_bytes))

        img = Image.open(file_like)
        img.show()
