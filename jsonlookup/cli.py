""" Commandline Interface """
import logging
from .setup_logging import setup_logging

import click


@click.command()
def main():
    """ Lookup and correlate JSON key, value pairs"""
    setup_logging()
    logging.info('being')


if __name__ == '__main__':
    main()
