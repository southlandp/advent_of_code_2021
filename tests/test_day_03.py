"""
.. codeauthor: Peter Southland
tests for advent of code day 3
Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
"""

import pytest

from advent_code import day_03 as main


@pytest.mark.parametrize('test_input, expected', [
    (['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'], [22, 9, 198]),
])
def test_part1(test_input, expected):
    d = main.Diagnostic(test_input)
    gamma, epsilon = d.gamma_epsilon()
    assert [gamma, epsilon, gamma * epsilon] == expected


@pytest.mark.parametrize('test_input, expected', [
    (['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'],
     [23, 10, 230]),

])
def test_part2(test_input, expected):
    d = main.Diagnostic(test_input)
    o2 = d.o2_generator()
    co2 = d.co2_scrubber()
    assert [o2, co2, o2 * co2] == expected
