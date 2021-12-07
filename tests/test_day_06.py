"""
.. codeauthor: Peter Southland
tests for advent of code day 6
Day 6: Lanternfish
https://adventofcode.com/2021/day/6
"""

import pytest

from advent_code import day_06 as main


@pytest.mark.parametrize('test_input, days, expected', [
    (['3,4,3,1,2'], 18, 26),
    (['3,4,3,1,2'], 80, 5934),
])
def test_part1(test_input, days, expected):
    f = main.FishPopulation(test_input)
    assert f.population_model(days=days) == expected


@pytest.mark.parametrize('test_input, days, expected', [
    (['3,4,3,1,2'], 18, 26),
    (['3,4,3,1,2'], 80, 5934),
    (['3,4,3,1,2'], 256, 26984457539),

])
def test_part2(test_input, days, expected):
    f = main.FishPopulation(test_input)
    assert f.population_model(days=days) == expected
