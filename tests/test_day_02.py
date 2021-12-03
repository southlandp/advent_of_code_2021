"""
.. codeauthor: Peter Southland
tests for advent of code day 1
Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
"""

import pytest

from advent_code.day_02 import main

@pytest.mark.parametrize('test_input, expected', [
    (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'], 150),
    (['forward 5', 'down 5', 'forward 8', 'up 03', 'down 8', 'forward 2'], 150),
    (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2.0'], 150),
])
def test_eval(test_input, expected):
    s = main.Submarine()
    s.plot_course(test_input)
    assert s.sonar_ping() == expected


@pytest.mark.parametrize('test_input, expected', [
    (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'], 900),
    (['forward 5', 'down 5', 'forward 8', 'up 03', 'down 8', 'forward 2'], 900),
    (['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2.0'], 900),
])
def test_eval(test_input, expected):
    s = main.SubmarineV2()
    s.plot_course(test_input)
    assert s.sonar_ping() == expected
