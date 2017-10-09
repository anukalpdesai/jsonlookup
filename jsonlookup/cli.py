"""Commandline Interface"""

import logging
from .setup_logging import setup_logging

import click


@click.command()
@click.argument('src_json', type=click.Path(allow_dash=True), required=False)
@click.argument('ref_json', type=click.Path(allow_dash=True), required=False)
@click.option('-i', '--id', type=click.STRING,
              help='Take value of this key from src_json')
@click.option('-r', '--ref',
              help='Reference location in ref_json to perform lookup')
@click.option('-k', '--key',
              help='Lookup the value of this key in ref_json')
@click.option('-v', '--value',
              help='If value of --id and --key matches, insert this key,'
              ' value pair from ref_json into src_json')
def main(**kwds):
    """ Correlate values of --id in src_json and --key in ref_json
        and on positive match insert --value into src_json"""
    setup_logging()
    logging.debug(kwds)


if __name__ == '__main__':
    main()
