import logging
import time

from src.activemq.utils import SubIdGenerator
from src.activemq.dependencies import ActiveMqConnectionFactory
from src.activemq.manager import ActivemqWorkerManager
from src.activemq.worker import ActiveMqWorker
from src.conversion.dependencies import convert_image_listener
import src.config as config
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    awm : ActivemqWorkerManager = ActivemqWorkerManager(workers=[
        ActiveMqWorker(
            connection=ActiveMqConnectionFactory.create_connection(
                listener=convert_image_listener
                ),
            sub_id=SubIdGenerator.generate_next(),
            queue=config.ACTIVEMQ_CONVERT_IMAGE_QUEUE
        ),
        ])
    awm.submit_threadpool()
    
    # loop indefinitely
    while True:
        try: time.sleep(.05)
        except KeyboardInterrupt as e:
            logging.info(e)
            break
    awm.stop_threadpool()

if __name__ == '__main__':
    main()
