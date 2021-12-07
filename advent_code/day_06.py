"""
.. codeauthor: Peter Southland
code for advent of code day 6
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""

from advent_code.common import functions

DAY = '06'


class FishPopulation:
    """
    takes vent data and creates map

    :ivar raw_data: raw puzzle data
    :ivar fish: counts of current fish population
    """

    def __init__(self, data):
        self.raw_data = data
        self.fish = [0] * 9

        self._read_input()

    def _read_input(self):
        """parses input into ivars"""

        for row in self.raw_data:

            for fish_age in map(int, row.split(',')):
                self.fish[fish_age] += 1

    def population_model(self, days=80):
        """
        models the number of fish at the end of days

        :param days: days to model for
        :type days: int

        """
        for i in range(days):

            new_fish = [0] * 9
            for age, fish in enumerate(self.fish):
                if age == 0:
                    new_fish[8] += fish
                    new_fish[6] += fish
                else:
                    new_fish[age - 1] += fish
            self.fish = new_fish

        return sum(self.fish)


if __name__ == '__main__':
    rows = functions.read_file()
    f = FishPopulation(rows)
    print(f.population_model())

    f = FishPopulation(rows)
    print(f.population_model(256))
