
import stomp

import src.config as config
from src.activemq.dispatcher import ActivemqDispatcher
from src.activemq.factory import ActiveMqConnectionFactory

send_conn = ActiveMqConnectionFactory.create_connection(
        broker_host=config.ACTIVEMQ_HOST,
        broker_port=config.ACTIVEMQ_PORT,
        broker_username=config.ACTIVEMQ_USERNAME,
        broker_password=config.ACTIVEMQ_PASSWORD,
        listener=None
    )

activemq_dispatcher = ActivemqDispatcher(conn=send_conn)
