from functools import reduce
import numpy as np
import math
from itertools import permutations
import copy
from collections import deque
from scipy.ndimage import convolve

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return list([[int(y) for y in x] for x in raw_data.strip().split('\n')])

def solve_p1(raw_data):
    original_data = process_input(raw_data)

    nx, ny = len(original_data[0]), len(original_data)

    data = [[np.inf for _ in range(0, nx+2)] for _ in range(0, ny+2)]

    for i in range(len(original_data)):
        for j in range(len(original_data[0])):
            data[i+1][j+1] = original_data[i][j]
    # print(data)
    result = []

    # counted = {}

    # print(nx, ny)

    # print(data)
    for i in range(1, ny+1):
        for j in range(1, nx+1):
            # print(i, j, data[i][j])
            # print(data[j][i])
            # if data[j][i] > data[j-1][i-1]:
                # continue
            
            if data[i][j] >= data[i-1][j]:
                continue
            if data[i][j] >= data[i][j-1]:
                continue
            if data[i][j] >= data[i+1][j]:
                continue
            if data[i][j] >= data[i][j+1]:
                continue
            
            # print(data[i-1][j])
            # print(data[i][j-1], data[i][j], data[i][j+1])
            # print(data[i+1][j])

            # if (j, i) in counted:
                # continue
            # counted[(j, i)] = True
            result.append(data[i][j] + 1)

    return np.sum(result)

def solve_p2(raw_data):
    original_data = process_input(raw_data)

    nx, ny = len(original_data[0]), len(original_data)

    data = [[9 for _ in range(0, nx+2)] for _ in range(0, ny+2)]

    for i in range(len(original_data)):
        for j in range(len(original_data[0])):
            data[i+1][j+1] = original_data[i][j]
    basins = [[0 for _ in range(0, nx+2)] for _ in range(0, ny+2)]

    # kernel = np.array([[1, 1, 1],
    #                   [1, 0, 1],
    #                   [1, 1, 1]])

    # print(convolve(convolve(basins, kernel, mode='constant'), kernel, mode='constant'))

    for _ in range(0, 10):
        for i in range(1, ny+1):
            for j in range(1, nx+1):
                if data[i][j] == 9:
                    continue
                basins[i][j] = 1
                

                if data[i][j] >= data[i-1][j]:
                    continue
                if data[i][j] >= data[i][j-1]:
                    continue
                if data[i][j] >= data[i+1][j]:
                    continue
                if data[i][j] >= data[i][j+1]:
                    continue
                
                # if data[i][j] > 0:
                
                data[i][j] = 9

                # if basins[i+1][j] > 0:
                #     basins[i][j] += basins[i+1][j]
                # if basins[i-1][j] > 0:
                #     basins[i][j] += basins[i-1][j]
                # if basins[i][j+1] > 0:
                #     basins[i][j] += basins[i][j+1]
                # if basins[i][j-1] > 0:
                #     basins[i][j] += basins[i][j-1]

    basin = 0
    basins_result = []

    print(np.array(basins))

    def calculate_basins(i, j):
        basin = 0

        if i < 1 or i > ny or j < 1 or j > nx:
            return 0

        if basins[i][j] == 0:
            basin = 0
            return 0
        elif basins[i][j] == 1:
            basin = 1
            basins[i][j] = 0

        if basins[i+1][j] == 1:
            # basins[i][j] += 1
            basin += calculate_basins(i+1, j)
        
        if basins[i-1][j] == 1:
            # basins[i][j] += 1
            basin += calculate_basins(i-1, j)
        
        if basins[i][j-1] == 1:
            # basins[i][j] += 1
            basin += calculate_basins(i, j-1)

        if basins[i][j+1] == 1:
            # basins[i][j] += 1
            basin += calculate_basins(i, j+1)

        return basin

    for _ in range(1):
        for i in range(1, ny+1):
            for j in range(1, nx+1):
                basins[i][j] = calculate_basins(i, j)

    print(np.array(basins))
    # diff = np.diff(data)
    # basins_result = []
    # basin = 0

    # for i in range(1, len(diff)-1):
    #     for j in range(1, len(diff[i])-1):
    #         if diff[i][j] != 1.0:
    #             basins_result.append(basin)
    #             basin = 0
    #             continue
    #         if diff[i-1][j] == 1.0:
    #             basin += 1
    #         if diff[i][j-1] == 1.0:
    #             basin += 1
    #         if diff[i+1][j] == 1.0:
    #             basin += 1
    #         if diff[i][j+1]:
    #             basin += 1

    sort = np.sort(np.array(basins).flatten())
    print(sort)
    print(sort[-1], sort[-2], sort[-3])
    return sort[-1] * sort[-2] * sort[-3]