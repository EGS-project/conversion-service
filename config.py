'''THIS FILE IS SAFE TO PUSH'''

from dotenv import find_dotenv, load_dotenv
from os import environ as env

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# AUTH VARIABLES
AUTH_CLIENT_ID=env.get('AUTH_CLIENT_ID', 'this is')
AUTH_CLIENT_SECRET=env.get('AUTH_CLIENT_SECRET', 'default variable')

# DATABASE VARIABLES
DATABASE_URL=env.get('DATABASE_URL', 'value if')
DATABASE_PORT=env.get('DATABASE_PORT', 'environment variable')

# APP VARIABLES
APP_SECRET_KEY=env.get('APP_SECRET_KEY', 'was not found or loaded')
