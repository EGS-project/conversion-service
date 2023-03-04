import config
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    logging.info('Now I can access the variables from the app\'s code!')
    logging.info(f'''
                 AUTH_CLIENT_ID -> {config.AUTH_CLIENT_ID},
                 AUTH_CLIENT_SECRET -> {config.AUTH_CLIENT_SECRET},
                 DATABASE_URL -> {config.DATABASE_URL},
                 DATABASE_PORT -> {config.DATABASE_PORT},
                 APP_SECRET_KEY -> {config.APP_SECRET_KEY}
                 ''')

if __name__ == '__main__':
    main()
