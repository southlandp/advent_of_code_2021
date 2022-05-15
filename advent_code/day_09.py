"""
.. codeauthor: Peter Southland
code for advent of code day 9
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""

from advent_code.common import functions

DAY = '09'


class LavaBasin:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    :ivar crabs: current horizontal distance of crabs
    """

    def __init__(self, data):
        self.raw_data = data
        self.points = []
        self.point_stats = {}

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""
        for row in self.raw_data:
            self.points.append(list(map(int, list(row))))

        for index, row in enumerate(self.points):
            for position, col in enumerate(row):
                point_key = f'{index}_{position}'
                self.point_stats[point_key] = {'value': col,
                                               'points': []}

                # north
                if index - 1 >= 0:
                    self.point_stats[point_key]['points'].append(self.points[index - 1][position])
                # south
                if index + 1 < len(self.points):
                    self.point_stats[point_key]['points'].append(self.points[index + 1][position])
                # east
                if position + 1 < len(row):
                    self.point_stats[point_key]['points'].append(self.points[index][position + 1])
                # west
                if position - 1 >= 0:
                    self.point_stats[point_key]['points'].append(self.points[index][position - 1])

    def local_min(self):
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
