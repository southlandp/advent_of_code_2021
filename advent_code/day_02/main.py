"""
.. codeauthor: Peter Southland
code for advent of code day 2
Day 2: Dive!
https://adventofcode.com/2021/day/2
"""

import os
from pathlib import Path
import re

from ..common import functions


class Submarine:
    """
    tracks submarine position

    :ivar horizontal: horizontal distance of submarine
    :ivar depth: depth of submarine
    """

    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def _forward(self, value):
        self.horizontal += value

    def _down(self, value):
        self.depth += value

    def _up(self, value):
        self.depth -= value

    def plot_course(self, rows):
        for row in rows:
            value = sum(int(x) for x in re.findall(r'\d+', row))

            if re.search(r'forward', row):
                self._forward(value)
            elif re.search(r'down', row):
                self._down(value)
            elif re.search(r'up', row):
                self._up(value)

    def sonar_ping(self):
        return self.depth * self.horizontal


class SubmarineV2:
    """
    tracks submarine position

    :ivar horizontal: horizontal distance of submarine
    :ivar depth: depth of submarine
    :ivar aim: aim of submarine
    """

    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def _forward(self, value):
        self.horizontal += value
        self.depth += value * self.aim

    def _down(self, value):
        self.aim += value

    def _up(self, value):
        self.aim -= value

    def plot_course(self, rows):
        for row in rows:
            value = sum(int(x) for x in re.findall(r'\d+', row))

            if re.search(r'forward', row):
                self._forward(value)
            elif re.search(r'down', row):
                self._down(value)
            elif re.search(r'up', row):
                self._up(value)

    def sonar_ping(self):
        return self.depth * self.horizontal


if __name__ == '__main__':
    rows = functions.read_file(os.path.join(Path(__file__).resolve().parent, 'input.txt'))

    s = Submarine()
    s.plot_course(rows)
    print(s.sonar_ping())

    s2 = SubmarineV2()
    s2.plot_course(rows)
    print(s2.sonar_ping())
