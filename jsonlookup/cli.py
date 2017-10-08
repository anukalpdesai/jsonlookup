""" Commandline Interface """
import logging
from setup_logging import setup_logging


def main():
    logging.info('being')


if __name__ == '__main__':
    setup_logging()
    main()
