"""
.. codeauthor: Peter Southland
code for advent of code day 8
Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8
"""

from advent_code.common import functions

DAY = '08'


class Display:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    :ivar crabs: current horizontal distance of crabs
    """

    def __init__(self, data):
        self.raw_data = data
        self.displays = {}

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""

        for i, row in enumerate(self.raw_data):

            vals = row.split('|')
            self.displays[i] = {'segments': vals[0].split(),
                                'outputs': vals[1].split()
                                }

    def read_display(self):
        count = 0
        for display in self.displays:
            for output in self.displays[display]['outputs']:
                if len(output) in (2, 3, 4, 7):
                    count += 1

        return count

    def calculate_digits(self):
        for display in self.displays:

    @staticmethod
    def _wire_logic(segments):
        wires = {'a': None,
                 'b': None,
                 'c': None,
                 'd': None,
                 'e': None,
                 'f': None,
                 'g': None}
        for segment in self.displays[display]['segments']:
            numbers[segment] = None
        for




if __name__ == '__main__':
    rows = functions.read_file()
    d = Display(rows)
    print(d.read_display())
    # print(c.find_optimal_location_complex())
