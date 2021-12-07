"""
.. codeauthor: Peter Southland
tests for advent of code day 5
Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5
"""

import pytest

from advent_code import day_05 as main


@pytest.mark.parametrize('test_input, expected', [
    (['0,9 -> 5,9',
      '8,0 -> 0,8',
      '9,4 -> 3,4',
      '2,2 -> 2,1',
      '7,0 -> 7,4',
      '6,4 -> 2,0',
      '0,9 -> 2,9',
      '3,4 -> 1,4',
      '0,0 -> 8,8',
      '5,5 -> 8,2'], 5),
])
def test_part1(test_input, expected):
    m = main.Mapping(test_input)
    assert m.cartography() == expected


@pytest.mark.parametrize('test_input, expected', [
    (['0,9 -> 5,9',
      '8,0 -> 0,8',
      '9,4 -> 3,4',
      '2,2 -> 2,1',
      '7,0 -> 7,4',
      '6,4 -> 2,0',
      '0,9 -> 2,9',
      '3,4 -> 1,4',
      '0,0 -> 8,8',
      '5,5 -> 8,2'], 12),

])
def test_part2(test_input, expected):
    m = main.Mapping(test_input)
    assert m.cartographyv2() == expected
