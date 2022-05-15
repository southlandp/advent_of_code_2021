"""
.. codeauthor: Peter Southland
tests for advent of code day 9
Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
"""

import pytest

from advent_code import day_09 as main


@pytest.mark.parametrize('test_input, expected', [
    (['2199943210',
      '3987894921',
      '9856789892',
      '8767896789',
      '9899965678'], 15),
])
def test_part1(test_input, expected):
    l = main.LavaBasin(test_input)
    assert l.local_min() == expected


# @pytest.mark.parametrize('test_input, expected', [
#     ('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe', 8394),
#     ('edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc', 9781),
#     ('fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg', 197),
#     ('fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb', 9361),
#     ('aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea', 4873),
#     ('fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb', 8418),
#     ('dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe', 4548),
#     ('bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef', 1625),
#     ('egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb', 8717),
#     ('gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce', 4315)
# ])
# def test_part2(test_input, expected):
#     d = main.Display(test_input)
#     assert b.throw_game() == expected
