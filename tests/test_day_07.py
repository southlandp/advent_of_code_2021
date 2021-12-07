"""
.. codeauthor: Peter Southland
tests for advent of code day 7
Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
"""

import pytest

from advent_code import day_07 as main


@pytest.mark.parametrize('test_input, expected', [
    (['16,1,2,0,4,2,7,1,2,14'], 37),
])
def test_part1(test_input, expected):
    c = main.Crabs(test_input)
    assert c.find_optimal_location_simple() == expected


@pytest.mark.parametrize('test_input, expected', [
    (['16,1,2,0,4,2,7,1,2,14'], 168),
])
def test_part2(test_input, expected):
    c = main.Crabs(test_input)
    assert c.find_optimal_location_complex() == expected
