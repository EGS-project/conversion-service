import logging
from io import BytesIO

import stomp
import stomp.utils
from PIL import Image

from src.activemq.dispatcher import ActivemqDispatcher
from src.conversion.converter import Converter
from src.conversion.message import ConvertImageMsg, ConvertImageReplyMsg


class ConvertImageListener(stomp.ConnectionListener):
    def __init__(self, dispatcher: ActivemqDispatcher) -> None:
        self.dispatcher = dispatcher
        
    def on_message(self, frame: stomp.utils.Frame):
        msg = ConvertImageMsg()
        msg.deserialize(frame=frame)
        logging.info(f'Message received: {msg}')
        # local debug
        # image = Image.open(BytesIO(msg.image_data))
        # image.show()
        
        # convert the image
        converted_image_data = Converter.convert(msg.image_data, msg.image_format)

        # reply
        self.dispatcher.send_convert_image_reply_message(
            ConvertImageReplyMsg(
                image_data=converted_image_data,
                correlation_id=msg.correlation_id
            )
        )
        
