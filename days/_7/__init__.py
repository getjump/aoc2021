from functools import reduce
import numpy as np
import math

def solve_p1(raw_data):
    data = np.array(list(map(int, raw_data.strip().split(','))), dtype=np.int64)
    return np.sum(np.abs(data - np.median(data)))

def solve_p2(raw_data):
    data = np.array(list(map(int, raw_data.strip().split(','))), dtype=np.int64)
    calcf = lambda n: int(n * (n + 1) / 2)
    mid = int(len(data)/2)
    print(np.mean(data))
    return np.sum(list(map(calcf, np.abs(data - np.mean(data)))))