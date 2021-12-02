from functools import reduce
import numpy as np

def solve_p1(raw_data):
    data = list(map(int, raw_data.split('\n')))
    return len(list(filter(lambda x: x > 0, np.diff(data))))

def solve_p2(raw_data):
    data = list(map(int, raw_data.split('\n')))
    data = [data[x] + data[x + 1] + data[x + 2] for x in range(0, len(data) - 2)]
    return len(list(filter(lambda x: x > 0, np.diff(data))))