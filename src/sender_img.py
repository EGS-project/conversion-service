import stomp.connect as connect
from src.message.utils import prepare_message
from src.activemq.factory import ActiveMqConnectionFactory
import src.config as config
import logging

conn: connect.StompConnection11 = ActiveMqConnectionFactory.create_connection(
    broker_host=config.ACTIVEMQ_HOST,
    broker_port=config.ACTIVEMQ_PORT,
    broker_username=config.ACTIVEMQ_USERNAME,
    broker_password=config.ACTIVEMQ_PASSWORD,
    listener=None
)

conn.send(
    body=prepare_message('./sample_images/anemone.png'),
    destination=config.ACTIVEMQ_CONVERT_IMAGE_QUEUE, 
    headers={'my-custom-header': 'custom-header_dataaa'}
    )
