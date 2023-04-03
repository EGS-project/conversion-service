from src.message.utils import parse_message
import src.config as config

from src.activemq.factory import ActiveMqConnectionFactory
from src.activemq.worker import ActiveMqWorker
from src.activemq.utils import SubIdGenerator
import stomp.connect as connect
from src.service import ConversionsListener
import logging
logging.basicConfig(level=logging.INFO)

conn: connect.StompConnection11 = ActiveMqConnectionFactory.create_connection(
    broker_host=config.ACTIVEMQ_HOST,
    broker_port=config.ACTIVEMQ_PORT,
    broker_username=config.ACTIVEMQ_USERNAME,
    broker_password=config.ACTIVEMQ_PASSWORD,
    listener=ConversionsListener()
)
logging.info("connected")

worker: ActiveMqWorker = ActiveMqWorker(
    connection=conn,
    sub_id=SubIdGenerator.generate_next(),
    queue=config.ACTIVEMQ_CONVERT_IMAGE_QUEUE
)
logging.info("subscribed")

worker.loop()
logging.info("exited")
