from functools import reduce
import numpy as np
import math
from itertools import permutations

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return list(raw_data.strip().split('\n'))

def parse_line(line):
    parsed = []

    nest_level = 0
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    inverse_symbols = {'}': '{', ']': '[', ')': '(', '>': '<'}

    for symbol in line:
        # print(parsed, symbol)
        if symbol in ['}', ']', ')', '>']:
            if parsed[nest_level-1] != inverse_symbols[symbol]:
                return points[symbol]
            nest_level -= 1
            del parsed[nest_level]
        elif symbol in ['{', '<', '(', '[']:
            nest_level += 1
            parsed.append(symbol)

    return 0

def complete_line(line):
    parsed = []

    nest_level = 0
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    points = 0

    inverse_symbols = {'}': '{', ']': '[', ')': '(', '>': '<'}
    symbols = {v: k for k, v in inverse_symbols.items()}

    lookup_points = {')': 1, ']': 2, '}': 3, '>': 4}

    for symbol in line:
        # print(parsed, symbol)
        if symbol in ['}', ']', ')', '>']:
            if parsed[nest_level-1] != inverse_symbols[symbol]:
                return points[symbol]
            nest_level -= 1
            del parsed[nest_level]
        elif symbol in ['{', '<', '(', '[']:
            nest_level += 1
            parsed.append(symbol)

    result = ''

    print(parsed)

    while parsed:
        points *= 5
        p = parsed.pop()
        result = p + result + symbols[p]
        print(symbols[p], lookup_points[symbols[p]], points)
        points += lookup_points[symbols[p]]

    return points

def solve_p1(raw_data):
    data = process_input(raw_data)
    result = 0

    for line in data:
        # print(line)
        result += parse_line(line)
    return result

def solve_p2(raw_data):
    data = process_input(raw_data)

    result = []
    incomplete_lines = []

    for line in data:
        parsed = parse_line(line)
        if parsed == 0:
            incomplete_lines.append(line)
            result.append(complete_line(line))

    return np.median(sorted(result, reverse=True))