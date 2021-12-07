"""
.. codeauthor: Peter Southland
tests for advent of code day 4
Day 4: Giant Squid
https://adventofcode.com/2021/day/4
"""

import pytest

from advent_code import day_04 as main


@pytest.mark.parametrize('test_input, expected', [
    (['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
      '',
      '22 13 17 11  0',
      ' 8  2 23  4 24',
      '21  9 14 16  7',
      ' 6 10  3 18  5',
      ' 1 12 20 15 19',
      '',
      ' 3 15  0  2 22',
      ' 9 18 13 17  5',
      '19  8  7 25 23',
      '20 11 10 24  4',
      '14 21 16 12  6',
      '',
      '14 21 17 24  4',
      '10 16 15  9 19',
      '18  8 23 26 20',
      '22 11 13  6  5',
      ' 2  0 12  3  7'], 4512),
])
def test_part1(test_input, expected):
    b = main.BingoGame(test_input)
    assert b.run_game() == expected


@pytest.mark.parametrize('test_input, expected', [
    (['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
      '',
      '22 13 17 11  0',
      ' 8  2 23  4 24',
      '21  9 14 16  7',
      ' 6 10  3 18  5',
      ' 1 12 20 15 19',
      '',
      ' 3 15  0  2 22',
      ' 9 18 13 17  5',
      '19  8  7 25 23',
      '20 11 10 24  4',
      '14 21 16 12  6',
      '',
      '14 21 17 24  4',
      '10 16 15  9 19',
      '18  8 23 26 20',
      '22 11 13  6  5',
      ' 2  0 12  3  7'], 1924),

])
def test_part2(test_input, expected):
    b = main.BingoGame(test_input)
    assert b.throw_game() == expected
