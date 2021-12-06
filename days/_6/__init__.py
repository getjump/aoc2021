from functools import reduce
import numpy as np

def solve_p1(raw_data):
    data = list(map(int, raw_data.strip().split(',')))

    for _ in range(0, 80):
        i = 0
        new_fishes = [x for x in data]
        while i < len(data):
            new_fishes[i] -= 1
            if new_fishes[i] < 0:
                new_fishes[i] = 6
                new_fishes.append(8)
            i += 1
        data = new_fishes

    return len(data)

def solve_p2(raw_data):
    data = list(map(int, raw_data.strip().split(',')))

    MAX_STATE = 8
    
    state = np.zeros(MAX_STATE+1, dtype=np.int64)
    for x in data:
        state[x] += 1

    for _ in range(0, 256):
        state = np.roll(state, -1)
        state[6] += state[8]
    return np.sum(state)