from functools import reduce
from typing import DefaultDict
import numpy as np
import math
from itertools import permutations
import copy
from collections import defaultdict
from numpy.core.fromnumeric import resize
from numpy.lib.nanfunctions import nanquantile
import llist
import heapq
from queue import PriorityQueue
import re
import numpy as np

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    matches = re.findall(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", raw_data)
    x0, x1, y0, y1 = map(int, matches[0])
    return x0, x1, y0, y1

def solve_p1(raw_data):    
    x0, x1, y0, y1 = process_input(raw_data)
    _map = [[0 for _ in range(100)] for _ in range(100)]

    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    print(x0, x1, y0, y1)
    initial_position = [0, 0]
    sol = []

    maxy = 0

    for i in range(-300, 300, 1):
        for j in range(-300, 300, 1):
            velocity = [i, j]
            position = [initial_position[0], initial_position[1]]
            maxy = 0
            for step in range(0, 5000):
                position[0] += velocity[0]
                position[1] += velocity[1]

                if position[0] > maxy:
                    maxy = position[0]

                if velocity[1] > 0:
                    velocity[1] -= 1
                elif velocity[1] < 0:
                    velocity[1] += 1

                velocity[0] -= 1
                if x0 <= position[1] <= x1 and y0 <= position[0] <= y1:
                # if initial_position[0] + j <= x1 and initial_position[0] + j >= x0 and initial_position[1] + i <= y0 and initial_position[1] + i >= y1:
                    # print(i, j)
                    sol.append(maxy)
                    break

                if position[0] < y0:
                    break
    
    print(sol)
    return max(sol)

def solve_p2(raw_data):
    x0, x1, y0, y1 = process_input(raw_data)
    _map = [[0 for _ in range(100)] for _ in range(100)]

    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    print(x0, x1, y0, y1)
    initial_position = [0, 0]
    sol = []

    maxy = 0

    for i in range(-300, 300, 1):
        for j in range(-300, 300, 1):
            velocity = [i, j]
            position = [initial_position[0], initial_position[1]]
            maxy = 0
            for step in range(0, 5000):
                position[0] += velocity[0]
                position[1] += velocity[1]

                if position[0] > maxy:
                    maxy = position[0]

                if velocity[1] > 0:
                    velocity[1] -= 1
                elif velocity[1] < 0:
                    velocity[1] += 1

                velocity[0] -= 1
                if x0 <= position[1] <= x1 and y0 <= position[0] <= y1:
                # if initial_position[0] + j <= x1 and initial_position[0] + j >= x0 and initial_position[1] + i <= y0 and initial_position[1] + i >= y1:
                    # print(i, j)
                    sol.append([i, j])
                    break

                if position[0] < y0:
                    break

    return len(sol)
