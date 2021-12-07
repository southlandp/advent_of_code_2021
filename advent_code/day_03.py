"""
.. codeauthor: Peter Southland
code for advent of code day 3
Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

from advent_code.common import functions

DAY = '03'


class Diagnostic:
    """
    diagnostic for submarine

    :ivar rows: default input rows

    .. todo:: clean this up, this solution is too messy
    """

    def __init__(self, rows):
        self.rows = rows

    def gamma_epsilon(self):
        """
        calculate gamma and epsilon diagnostics

        :return: gamma and epsilon rate
        :type: tuple
        """
        gamma_rate = []
        epsilon_rate = []
        for i in range(len(self.rows[0])):
            counts = self._bit_criteria(self.rows, i)
            if counts['0'] > counts['1']:
                gamma_rate.append('0')
                epsilon_rate.append('1')
            else:
                gamma_rate.append('1')
                epsilon_rate.append('0')

        gamma_rate = int(''.join(gamma_rate), 2)
        epsilon_rate = int(''.join(epsilon_rate), 2)
        return gamma_rate, epsilon_rate

    @staticmethod
    def _bit_criteria(rows, column):
        """
        determines bitrate stats for current columns of rows

        :param rows: rows to check for bit criteria
        :type rows: list
        :param column: column in row to check
        :type column: int

        :return: bitrate statistics
        :type: dict
        """
        counts = {'0': 0, '1': 0, 'biggest': '1', 'smallest': '0'}
        for row in rows:
            if row[column] == '1':
                counts['1'] += 1
            else:
                counts['0'] += 1

        if counts['0'] > counts['1']:
            counts['biggest'] = '0'
            counts['smallest'] = '1'
        else:
            counts['biggest'] = '1'
            counts['smallest'] = '0'

        return counts

    def o2_generator(self):
        """calculates o2 generator stats"""
        rows = self.rows.copy()
        bit_length = len(rows[0])
        for i in range(bit_length):
            counts = self._bit_criteria(rows, i)
            rows = self._scanner(rows, counts['biggest'], i)

            if len(rows) <= 1:
                break

        return int(rows[0], 2)

    def co2_scrubber(self):
        """calculates co2 scrubber stats"""
        rows = self.rows.copy()
        bit_length = len(rows[0])
        for i in range(bit_length):
            counts = self._bit_criteria(rows, i)
            rows = self._scanner(rows, counts['smallest'], i)

            if len(rows) <= 1:
                break

        return int(rows[0], 2)

    @staticmethod
    def _scanner(rows, bit, column):
        """
        removes rows that do not match the current bit rate

        :param rows: rows to check for bit matches
        :type rows: list
        :param bit: bit value 0 or 1
        :type bit: str
        :param column: column in row to check
        :type column: int

        :return: bitrate statistics
        :type: dict
        """
        new_rows = []
        for row in rows:
            if row[column] == bit:
                new_rows.append(row)

        return new_rows


if __name__ == '__main__':
    rows = functions.read_file()

    d = Diagnostic(rows)
    gamma, epsilon = d.gamma_epsilon()
    print(gamma * epsilon)

    o2 = d.o2_generator()
    co2 = d.co2_scrubber()
    print(o2 * co2)
