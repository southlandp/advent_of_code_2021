"""
.. codeauthor: Peter Southland
tests for advent of code day 1
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
"""

import pytest

from day_01 import main

@pytest.mark.parametrize('test_input, expected', [
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
    ([199, 200, 208, 210, 200, 200, 207, 240, 269, 260, 263], 7),
    ([199, 200, 208, 210, 200, 200, 240, 269, 260, 263], 6),
    (['9', '200', '208', '210', '200', '207', '240', '269', '260', '263'], 7),
    (['9', '200', '208', '210', '200', '200', '207', '240', '269', '260', '263'], 7),
    (['9', '200', '208', '210', '200', '190', '240', '269', '260', '263'], 6)
])
def test_eval(test_input, expected):
    assert main.sonar_sweep(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5),
    ([199, 200, 208, 210, 200, 200, 207, 240, 269, 260, 263], 5),
    ([199, 200, 208, 210, 200, 200, 240, 269, 260, 263], 5),
    (['9', '200', '208', '210', '200', '207', '240', '269', '260', '263'], 5),
    (['9', '200', '208', '210', '200', '200', '207', '240', '269', '260', '263'], 5),
    (['9', '200', '208', '210', '200', '190', '240', '269', '260', '263'], 5)
])
def test_eval(test_input, expected):
    assert main.sonar_sweep_moving_average(test_input) == expected
