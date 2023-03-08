'''THIS FILE IS SAFE TO PUSH'''

from dotenv import find_dotenv, load_dotenv
from os import environ as env

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# RABBIT_MQ
RABBIT_MQ_HOST = env.get('RABBIT_MQ_HOST', 'localhost')
RABBIT_MQ_PORT = int(env.get('RABBIT_MQ_PORT', '1883'))
RABBIT_MQ_USERNAME = env.get('RABBIT_MQ_USERNAME', '')
RABBIT_MQ_PASSWORD = env.get('RABBIT_MQ_PASSWORD', 'mypassword')
RABBIT_MQ_SSL = env.get('RABBIT_MQ_SSL', '')

# RABBIT_MQ QUEUES
RABBIT_MQ_EXCHANGE_NAME = env.get('RABBIT_MQ_EXCHANGE_NAME', 'deault_exchange')
RABBIT_MQ_QUEUE_NAME = env.get('RABBIT_MQ_QUEUE_NAME', 'default_queue')