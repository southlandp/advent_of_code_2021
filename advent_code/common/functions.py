"""
.. codeauthor: Peter Southland
common reusable functions
"""

import logging


# def get_logger():
#     logging.basicConfig(level='INFO', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#     logger = logging.getLogger(__name__)


def read_file(file_name):
    """
    reads file and returns all lines as a list of strings

    :param file_name: file path
    :type: file_name: str

    :return: list of strings containing file contents
    :rtype: list
    """

    with open(file_name, mode='r', encoding='utf-8') as f:
        return f.read().splitlines()
