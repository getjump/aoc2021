from functools import reduce
import numpy as np
import math
from itertools import permutations

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return [[int(x) for x in y] for y in raw_data.strip().split('\n')]

def flash_neighbours(data, flashed, i, j):
    result = 0

    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
        return result

    if flashed[i][j]:
        return result

    if data[i][j] >= 9:
        flashed[i][j] = True
        result += 1
        data[i][j] = 0
    else:
        data[i][j] += 1
        return result

    return result + flash_neighbours(data, flashed, i+1, j) + flash_neighbours(data, flashed, i-1, j) + flash_neighbours(data, flashed, i, j+1) + flash_neighbours(data, flashed, i, j-1) + flash_neighbours(data, flashed, i+1, j+1) + flash_neighbours(data, flashed, i-1, j-1) + flash_neighbours(data, flashed, i+1, j-1) + flash_neighbours(data, flashed, i-1, j+1)


def all_flashed(flashed):
    result = True
    for y in range(len(flashed)):
        for x in range(len(flashed)):
            if not flashed[y][x]:
                result = False
    return result

def solve_p1(raw_data):
    data = process_input(raw_data)
    result = 0
    for steps in range(100):
        flashed = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
        for y in range(len(data)):
            for x in range(len(data)):
                result += flash_neighbours(data, flashed, y, x)
    return result

def solve_p2(raw_data):
    data = process_input(raw_data)
    for step in range(1000):
        flashed = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
        for y in range(len(data)):
            for x in range(len(data)):
                flash_neighbours(data, flashed, y, x)
                if all_flashed(flashed):
                    return step+1
    return 0