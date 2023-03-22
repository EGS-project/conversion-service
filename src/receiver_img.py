from PIL import Image
import stomp
from src.message.utils import parse_message
import src.config as config
import time

from src.activemq.factory import ActiveMqConnectionFactory
from src.activemq.worker import ActiveMqWorker
from src.activemq.utils import SubIdGenerator
import stomp.connect as connect

import logging
logging.basicConfig(level=logging.INFO)

class ImageListener(stomp.ConnectionListener):
    def __init__(self):
        super().__init__()
        
    def on_message(self, message):
        image_data= parse_message(message)
        import io
        image = Image.open(io.BytesIO(image_data))
        image.show()
        

conn: connect.StompConnection11 = ActiveMqConnectionFactory.create_connection(
    broker_host=config.ACTIVEMQ_HOST,
    broker_port=config.ACTIVEMQ_PORT,
    broker_username=config.ACTIVEMQ_USERNAME,
    broker_password=config.ACTIVEMQ_PASSWORD,
    listener=ImageListener()
)

worker: ActiveMqWorker = ActiveMqWorker(
    connection=conn,
    sub_id=SubIdGenerator.generate_next(),
    queue=config.ACTIVEMQ_CONVERT_IMAGE_QUEUE
)
logging.info("subscribed")
worker.loop()
