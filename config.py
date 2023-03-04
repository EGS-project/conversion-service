'''THIS FILE IS SAFE TO PUSH'''

from dotenv import find_dotenv, load_dotenv
from os import environ as env

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# BROKER VARIABLES
ACTIVEMQ_HOST=env.get('ACTIVEMQ_HOST', 'value if')
ACTIVEMQ_PORT=env.get('ACTIVEMQ_PORT', 'environment variable')
