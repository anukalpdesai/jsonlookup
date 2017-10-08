""" Commandline Interface """
import logging
from .setup_logging import setup_logging


def main():
    setup_logging()
    logging.info('being')


if __name__ == '__main__':
    main()
