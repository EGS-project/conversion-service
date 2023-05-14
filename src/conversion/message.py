import email
from email.mime.image import MIMEImage
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import stomp.utils


class ConvertImageMsg():
    def __init__(
        self, 
        image_data: bytes = None, 
        image_format: str = None
        ) -> None:
        self.image_data = image_data
        self.image_format = image_format
        self.correlation_id: str = None

    def deserialize(self, frame: stomp.utils.Frame) -> None:
        mime_message: MIMEMessage = email.message_from_string(frame.body)
        for part in mime_message.walk():
            if part.get('Content-ID') == 'data':
                self.image_data = part.get_payload(decode=True)
            elif part.get('Content-ID') == 'image_format':
                self.image_format = part.get_payload(decode=False)
        self.correlation_id = frame.headers.get('correlation_id')

class ConvertImageReplyMsg():
    def __init__(
        self, 
        image_data: bytes = None,
        correlation_id: str = None
        ) -> None:
        self.image_data = image_data
        self.correlation_id = correlation_id
        
    def serialize(self):
        mime_multipart = MIMEMultipart()
        if self.image_data:
            part = MIMEImage(self.image_data)
            part.add_header('Content-ID', 'data')
            mime_multipart.attach(part)
        return mime_multipart.as_string()
