from PIL import Image
import stomp

from src.message.utils import parse_message


class ConversionsListener(stomp.ConnectionListener):
    def __init__(self):
        super().__init__()
        
    def on_message(self, message):
        image_data= parse_message(message)
        import io
        image = Image.open(io.BytesIO(image_data))
        image.show()
