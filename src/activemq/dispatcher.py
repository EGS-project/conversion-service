import stomp.connect as connect

import src.config as config
from src.conversion.message import *

class ActivemqDispatcher:
    def __init__(self, conn: stomp.StompConnection11) -> None:
        self.conn = conn
        
    def send_convert_image_reply_message(self, msg: ConvertImageReplyMsg) -> None:
        self.conn.send(
            destination=config.ACTIVEMQ_CONVERT_IMAGE_REPLY_QUEUE,
            body=msg.serialize(),
            headers={
                'content-type': 'multipart/mixed',
                'correlation_id': msg.correlation_id
            }
        )
    