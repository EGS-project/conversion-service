import stomp
import stomp.utils
import logging
from src.conversion.message import ConvertImageMsg, ConvertImageReplyMsg
from src.activemq.dispatcher import ActivemqDispatcher


class ConvertImageListener(stomp.ConnectionListener):
    def __init__(self, dispatcher: ActivemqDispatcher) -> None:
        self.dispatcher = dispatcher
        
    def on_message(self, frame: stomp.utils.Frame):
        msg = ConvertImageMsg()
        msg.deserialize(frame=frame)
        # for debug
        # with open('sample_images/reply.png', 'wb') as f:
        #     f.write(msg.image_data)
        
        # convert the image
        converted_image_data = ...
        
        # reply
        self.dispatcher.send_convert_image_reply_message(
            ConvertImageReplyMsg(
                image_data=converted_image_data,
                correlation_id=msg.correlation_id
            )
        )
