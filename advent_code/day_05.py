"""
.. codeauthor: Peter Southland
code for advent of code day 5
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5
"""

from advent_code.common import functions

DAY = '05'


class Mapping:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    :ivar vents: start and end points for vents
    :ivar map: matrix of vent locations
    :ivar highest_number: determines length and width of matrix
    """

    def __init__(self, data):
        self.raw_data = data
        self.vents = []
        self.map = []
        self.highest_number = 0

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""
        for row in self.raw_data:
            points = []

            for point in row.split(' -> '):
                points.append(tuple(map(int, point.split(','))))
            if points[0][0] > points[1][0]:
                points = [points[i] for i in [1, 0]]  # re-orders points so smallest x is always on the left
            self.vents.append(points)

        for vent in self.vents:
            for points in vent:
                for point in points:
                    if point > self.highest_number:
                        self.highest_number = point

        for i in range(self.highest_number + 1):
            self.map.append([0] * (self.highest_number+1))

    def cartography(self):
        """
        calculates overlap for vertical and horizontal lines

        ..todo:: need a cleaner solution this one is messy
        """
        for points in self.vents:
            start_y = points[0][1]
            end_y = points[1][1]
            start_x = points[0][0]
            end_x = points[1][0]

            # check if line is vertical
            if start_x == end_x:
                for i in range(min(start_y, end_y), max(start_y, end_y)+1):
                    self.map[i][start_x] += 1
            # check if line is horizontal
            elif start_y == end_y:
                for i in range(start_x, end_x+1):
                    self.map[start_y][i] += 1

        count = 0
        for line in self.map:
            for point in line:
                if point >= 2:
                    count += 1

        return count

    def cartographyv2(self):
        """
        calculates overlap for vertical, horizontal, and diagonal lines

        ..todo:: need a cleaner solution this one is messy
        """
        for points in self.vents:
            start_y = points[0][1]
            end_y = points[1][1]
            start_x = points[0][0]
            end_x = points[1][0]

            slope = 0
            if start_x != end_x:
                slope = int((end_y - start_y) / (end_x - start_x))

            # check if line is vertical
            if start_x == end_x:
                for i in range(min(start_y, end_y), max(start_y, end_y)+1):
                    self.map[i][start_x] += 1
            # check if line is horizontal
            elif start_y == end_y:
                for i in range(start_x, end_x + 1):
                    self.map[start_y][i] += 1
            # diagonal
            else:
                for i in range(start_x, end_x + 1):
                    self.map[start_y][i] += 1
                    start_y += slope

        count = 0
        for line in self.map:
            for point in line:
                if point >= 2:
                    count += 1

        return count


if __name__ == '__main__':
    rows = functions.read_file()
    m1 = Mapping(rows)
    print(m1.cartography())

    m2 = Mapping(rows)
    print(m2.cartographyv2())
