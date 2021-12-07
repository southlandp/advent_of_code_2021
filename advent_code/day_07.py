"""
.. codeauthor: Peter Southland
code for advent of code day 7
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""

from advent_code.common import functions

DAY = '07'


class Crabs:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    :ivar crabs: current horizontal distance of crabs
    """

    def __init__(self, data):
        self.raw_data = data
        self.crabs = []
        self.current_location = 0

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""

        for row in self.raw_data:

            for crab_distance in map(int, row.split(',')):
                self.crabs.append(crab_distance)

    def find_optimal_location_simple(self):
        """
        finds optimal location to move submarine based on crab locations

        :return: minimum fuel usage for crabs
        :rtype: int

        .. todo:: could be optimized to not calculate every location, maybe something like a binary search
        """
        fuel_usage = []
        for i in range(max(self.crabs)):
            fuel = 0
            for crab in self.crabs:
                fuel += abs(i - crab)
            fuel_usage.append(fuel)

        return min(fuel_usage)

    def find_optimal_location_complex(self):
        """
        finds optimal location to move submarine based on crab locations

        :return: minimum fuel usage for crabs
        :rtype: int

        .. todo:: could be optimized to not calculate every location, maybe something like a binary search
        """
        fuel_usage = []
        for i in range(max(self.crabs)):
            fuel = 0
            for crab in self.crabs:
                distance = abs(i - crab)
                fuel += int((distance * (distance + 1))/2)  # 1 + 2 + 3 + ... n
            fuel_usage.append(fuel)

        return min(fuel_usage)


if __name__ == '__main__':
    rows = functions.read_file()
    c = Crabs(rows)
    print(c.find_optimal_location_simple())
    print(c.find_optimal_location_complex())
