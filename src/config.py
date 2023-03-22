'''THIS FILE IS SAFE TO PUSH'''



from dotenv import find_dotenv, load_dotenv
from os import environ as env
import stomp

if ENV_FILE := find_dotenv():
    load_dotenv(ENV_FILE)

# ACTIVE_MQ CONNECTION
ACTIVEMQ_HOST = env.get('ACTIVEMQ_HOST', 'localhost')
ACTIVEMQ_PORT = env.get('ACTIVEMQ_PORT', '61613')
ACTIVEMQ_USERNAME = env.get('ACTIVEMQ_USERNAME', 'exposed')
ACTIVEMQ_PASSWORD = env.get('ACTIVEMQ_PASSWORD', 'credentials')

# ACTIVE_MQ QUEUES
ACTIVEMQ_CONVERT_IMAGE_EXCHANGE = env.get('ACTIVEMQ_CONVERT_IMAGE_EXCHANGE', 'aaa')
ACTIVEMQ_CONVERT_IMAGE_QUEUE = env.get('ACTIVEMQ_CONVERT_IMAGE_QUEUE', 'bbb')

# 

# SSL
SSL_ACTIVE = env.get('SSL_ACTIVE') == 1 
SSL_CERTFILE = env.get('SSL_CERTFILE', 'default/certfile.pem')
SSL_KEYFILE = env.get('SSL_KEYFILE', 'default/keyfile.pem')

SSL_PARAMS = {
    'ssl_version': stomp.ssl.PROTOCOL_TLS,
    'key_file': SSL_KEYFILE,
    'cert_file': SSL_CERTFILE
    } if SSL_ACTIVE else {}
