import src.config as config
import io
from src.conversion.message import ConvertImageMsg
from PIL import Image

from tests.activemq.dispatcher import TestingDispatcher
from src.activemq.factory import ActiveMqConnectionFactory

send_conn = ActiveMqConnectionFactory.create_connection(
        broker_host=config.ACTIVEMQ_HOST,
        broker_port=config.ACTIVEMQ_PORT,
        broker_username=config.ACTIVEMQ_USERNAME,
        broker_password=config.ACTIVEMQ_PASSWORD,
        listener=None
    )

activemq_dispatcher = TestingDispatcher(conn=send_conn)

img = Image.open('sample_images/test.png')
byte_stream = io.BytesIO()
img.save(byte_stream, format='PNG')

msg = ConvertImageMsg(byte_stream.getvalue(), 'JPEG')

activemq_dispatcher.send_convert_image_message(msg)
