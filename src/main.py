import config
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    logging.info('Now I can access the variables from the app\'s code!')
    logging.info(
        f'''
        ACTIVEMQ_HOST -> {config.ACTIVEMQ_HOST},
        ACTIVEMQ_PORT -> {config.ACTIVEMQ_PORT},
        ''')

if __name__ == '__main__':
    main()
