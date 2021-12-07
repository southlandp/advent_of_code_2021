"""
.. codeauthor: Peter Southland
code for advent of code day 4
Day 4: Giant Squid
https://adventofcode.com/2021/day/4
"""

import re

from advent_code.common import functions

DAY = '04'


class BingoGame:
    """
    runs bingo game

    :ivar raw_data: raw puzzle data
    :ivar numbers: numbers to be called during game
    :ivar boards: boards to run during game
    """

    def __init__(self, data):
        self.raw_data = data
        self.numbers = []
        self.boards = []

        self._read_input()

    def _read_input(self):
        """parses input"""
        bingo_lines = []
        for row in self.raw_data:

            if re.search(',', row):
                self.numbers = row.split(',')
                self.numbers = list(map(int, self.numbers))
            elif re.search(r'\d', row):
                line = row.split()
                bingo_lines.append(list(map(int, line)))
            elif bingo_lines:
                self.boards.append(BingoBoard(bingo_lines))
                bingo_lines = []
        self.boards.append(BingoBoard(bingo_lines))

    def run_game(self):
        """calls bingo numbers and picks first winner"""
        for num in self.numbers:
            for board in self.boards:
                if board.call_number(num) == 'Bingo!!':
                    return sum(board.numbers) * num

    def throw_game(self):
        """calls bingo numbers and picks last winner"""
        last_result = 0
        for num in self.numbers:
            for board in self.boards:
                if board.call_number(num) == 'Bingo!!':
                    last_result = sum(board.numbers) * num
        return last_result


class BingoBoard:
    """
    runs bingo game

    :ivar board: layout of board
    :ivar numbers: all numbers on board
    :ivar winner: True if board won, False if it's not a winner yet
    :ivar winner: valid_winds dict of all possible horizontal and vertical wins
    """

    def __init__(self, board):
        self.board = board
        self.numbers = set()
        self.winner = False

        self.valid_wins = {}

        for column in range(len(self.board[0])):
            for index, row in enumerate(self.board):
                if f'vertical_{index}' not in self.valid_wins:
                    self.valid_wins[f'vertical_{index}'] = set()
                self.valid_wins[f'horizontal_{index}'] = set(row)
                self.valid_wins[f'vertical_{column}'].add(row[column])
                self.numbers.add(row[column])

    def call_number(self, number):
        """checks if board has a number, marks it as no longer available and checks if there was a win"""
        if number in self.numbers and not self.winner:
            self.numbers.remove(number)

            for row in self.valid_wins:
                self.valid_wins[row].discard(number)
                if not self.valid_wins[row]:
                    self.winner = True
                    return 'Bingo!!'


if __name__ == '__main__':
    rows = functions.read_file()
    b = BingoGame(rows)
    print(b.run_game())
    print(b.throw_game())
