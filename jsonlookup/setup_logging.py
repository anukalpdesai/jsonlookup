""" This module sets up basic logging for jsonlookup """
import logging


def setup_logging(level=logging.DEBUG):
    format_string = '%(name)s:%(levelname)s:%(filename)s:%(funcName)s:'\
                    '%(lineno)d:%(msg)s'
    logging.basicConfig(level=level,
                        format=format_string)
