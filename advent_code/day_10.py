"""
.. codeauthor: Peter Southland
code for advent of code day 10
Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10
"""

from advent_code.common import functions

DAY = '10'


class SnytaxCheck:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    """

    def __init__(self, data):
        self.raw_data = data
        self.lines = []

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""
        for row in self.raw_data:
            self.lines.append(row)

    def validate(self):
        count = 0
        for point in self.point_stats:
            if self.point_stats[point]['value'] < min(self.point_stats[point]['points']):
                count += self.point_stats[point]['value'] + 1

        return count


if __name__ == '__main__':
    rows = functions.read_file()
    l = LavaBasin(rows)
    print(l.local_min())
    # print(c.find_optimal_location_complex())
