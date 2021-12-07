from functools import reduce
import numpy as np
import math

def solve_p1(raw_data):
    data = list(map(int, raw_data.strip().split(',')))

    best_result = np.inf
    for z in range(0, np.max(data)):
        result = 0
        for x in data:
            result += abs(x - z)
        if result < best_result:
            best_result = result

    return best_result

def solve_p2(raw_data):
    data = list(map(int, raw_data.strip().split(',')))

    calcf = lambda n: int(n * (n + 1) / 2)

    best_result = np.inf
    for z in range(0, np.max(data)):
        result = 0
        for x in data:
            result += calcf(abs(x - z))
        if result < best_result:
            best_result = result

    return best_result

    return np.sum(data)