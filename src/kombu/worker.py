import logging
from kombu.mixins import ConsumerMixin
from src.kombu.kombu_connection import KombuConnection

class Worker(ConsumerMixin):
    def __init__(self, connection: KombuConnection, queues):
        self.connection = connection
        self.queues = queues
    
    def get_consumers(self, Consumer, channel):
        return [
            Consumer(
                queues=self.queues,
                callbacks=[self.on_message],
                accept=[
                    'image/jpeg'
                    'application/json',
                    'application/x-python-serialize',
                    'pickle']
                )
            ]
    
    def on_message(self, body, message):
        # Get message headers' information
        msg_source = message.headers["source"]  
        
        logging.warn(f'Message: {message}') 
        
        # Remove Message From Queue
        message.ack()
    