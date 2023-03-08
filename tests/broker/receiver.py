'''In case of import issues, execute in terminal
export PYTHONPATH=$PWD
from main directory
'''
import logging
from src.kombu.worker import Worker
from src.kombu.kombu_connection import KombuConnection
import src.config as config

logging.basicConfig(level=logging.INFO)


class Receiver:
    def __init__(self) -> None:
        self.worker = None
    
    def start_processing(self, exchange_name, queue_name):
        self.worker = Worker(
            connection=KombuConnection.CONNECTION,
            queues=KombuConnection.get_queue(exchange_name, queue_name)
        )
        self.worker.run()

if __name__ == '__main__':
    KombuConnection.create_connection(
        broker_url="{}:{}".format(config.RABBIT_MQ_HOST, config.RABBIT_MQ_PORT),
        broker_username=config.RABBIT_MQ_USERNAME,
        broker_password=config.RABBIT_MQ_PASSWORD,
        ssl_active=config.RABBIT_MQ_SSL
        )
    Receiver().start_processing(exchange_name=config.RABBIT_MQ_EXCHANGE_NAME, queue_name=config.RABBIT_MQ_QUEUE_NAME)
