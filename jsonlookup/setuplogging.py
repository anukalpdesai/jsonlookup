""" This module sets up basic logging for jsonlookup """
import logging


def setup_logging(level=logging.DEBUG):
    format_string = '%(name)s:(%levelno)s:%(filename)s:%(funcName)s%(lineno)d'
    logging.basicConfig(level=level,
                        format=format_string)
