"""
.. codeauthor: Peter Southland
code for advent of code day 1
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
"""

import os
from pathlib import Path

from advent_code.common import functions

DAY = '01'


def sonar_sweep(rows):
    """
    counts the number of entries that have a higher value than the previous

    :param rows: list of depth values
    :type rows: list

    :return: number of entries in rows that have a higher value than the previous
    :rtype: int
    """

    current_depth = None
    depth_increases = 0
    for row in rows:
        row = int(row)
        if not current_depth:
            pass
        elif row > current_depth:
            depth_increases += 1
        current_depth = row

    return depth_increases


def sonar_sweep_moving_average(rows, window=3):
    """
    counts the number of entries that have a higheint(r value than the previous

    :param rows: list of depth values
    :type rows: list
    :param window: length of window for moving average
    :type window: int

    :return: number of entries in rows that have a higher value than the previous
    :rtype: int
    """

    current_depth = []
    depth_window = []
    depth_increases = 0
    for row in rows:
        depth_window.append(int(row))

        if len(depth_window) > window:
            depth_window.pop(0)

        if len(depth_window) < window or len(current_depth) < window:
            pass
        elif sum(depth_window) > sum(current_depth):
            depth_increases += 1
        current_depth = depth_window.copy()

    return depth_increases


if __name__ == '__main__':
    rows = functions.read_file()
    print(sonar_sweep(rows))
    print(sonar_sweep_moving_average(rows))
