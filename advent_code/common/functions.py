"""
.. codeauthor: Peter Southland
common reusable functions
"""

import os
from pathlib import Path


# import logging
#
#
# def get_logger():
#     logging.basicConfig(level='INFO', format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#     logger = logging.getLogger(__name__)


def read_file(file_name=None, return_type='raw'):
    """
    reads file and returns all lines as a list of strings

    :param file_name: file path
    :type: file_name: str
    :param return_type: defines the type of data that should be returned
    :type: return_type: str

    :return: list of strings containing file contents
    :rtype: list
    """
    if file_name is None:
        import __main__
        file_name = os.path.join(Path(__main__.__file__).resolve().parent, 'Data', f'day_{__main__.DAY}.txt')

    with open(file_name, mode='r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        if return_type == 'int':
            lines = list(map(int, lines))
        elif return_type == 'raw':
            pass
        else:
            raise NotImplementedError(f'return_type "{return_type}" is invalid')

        return lines
