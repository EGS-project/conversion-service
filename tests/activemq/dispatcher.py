import stomp.connect as connect

import src.config as config
from src.conversion.message import *
from src.activemq.dispatcher import ActivemqDispatcher

class TestingDispatcher(ActivemqDispatcher):
    def __init__(self, conn: stomp.StompConnection11) -> None:
        super().__init__(conn)
        
    def send_convert_image_message(self, msg: ConvertImageMsg) -> None:
        self.conn.send(
            destination=config.ACTIVEMQ_CONVERT_IMAGE_QUEUE,
            body=msg.serialize(),
            headers={
                'content-type': 'multipart/mixed',
                'correlation_id': msg.correlation_id
            }
        )
    