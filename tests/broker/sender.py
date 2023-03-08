'''In case of import issues, execute in terminal
export PYTHONPATH=$PWD
from main directory
'''
import json
import logging
from src.kombu.worker import Worker
from src.kombu.kombu_connection import KombuConnection
import src.config as config
from kombu.message import Message
import pickle

logging.basicConfig(level=logging.INFO)

class Sender:
    def publish_test_msg(self):
        message = json.dumps({
            'source': 'sender blabla',
            'xyz': 1231231,
            '123': 41221312
        })
           
        
        logging.info(f'Message sent: {message.__str__()}')
        
        producer = KombuConnection.get_producer(config.RABBIT_MQ_EXCHANGE_NAME, config.RABBIT_MQ_QUEUE_NAME)
        producer.publish(message, content_type='application/json')
        producer.close()


if __name__ == '__main__':
    KombuConnection.create_connection(
        broker_url="{}:{}".format(config.RABBIT_MQ_HOST, config.RABBIT_MQ_PORT),
        broker_username=config.RABBIT_MQ_USERNAME,
        broker_password=config.RABBIT_MQ_PASSWORD,
        ssl_active=config.RABBIT_MQ_SSL
        )
    Sender().publish_test_msg()
