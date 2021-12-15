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

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return [[int(x) for x in y] for y in raw_data.split('\n')]

def solve_p1(raw_data):    
    data = process_input(raw_data)

    risk_levels = []

    def bf(src):
        dist = {y: {x: np.inf for x in range(len(data[0]))} for y in range(len(data))}
        pred = {y: {x: (-1, -1) for x in range(len(data[0]))} for y in range(len(data))}
        
        dist[src[0]][src[1]] = 0

        def relax(v, u):
            if data[v[0]][v[1]] + dist[u[0]][u[1]] < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = data[v[0]][v[1]] + dist[u[0]][u[1]]
                pred[v[0]][v[1]] = u

        for _ in range(len(data) * len(data[0])):
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if i+1 < len(data):
                        relax([i, j], [i+1, j])
                    if i-1 >= 0:
                        relax([i, j], [i-1, j])

                    if j-1 >= 0:
                        relax([i, j], [i, j-1])
                    if j+1 < len(data[0]):
                        relax([i, j], [i, j+1])

        return dist, pred

    # def dfs(v, end, path=[]):
    #     if v in path:
    #         return

    #     if v[0] < 0 or v[0] >= len(data):
    #         return
    #     if v[1] < 0 or v[1] >= len(data[0]):
    #         return
        
    #     if v != [0, 0]:
    #         path = path + [v]
    #     if v == end:
    #         risk_levels.append(sum([data[x[0]][x[1]] for x in path]))
    #         return
        
    #     dfs([v[0]+1, v[1]], end, path)
    #     dfs([v[0]-1, v[1]], end, path)
    #     dfs([v[0], v[1]+1], end, path)
    #     dfs([v[0], v[1]-1], end, path)

    dist, pred = bf([0, 0])
    
    pathes = []
    
    # def shortest_path(current, target, pred, path=[]):
    #     if current == [-1, -1]:
    #         return path

    #     if current[0] == -1 or current[1] == -1:
    #         return path

    #     if current == target:
    #         path = path + [current]
    #         pathes.append(path)
    #         return path
    #     print(current[0], current[1], pred[current[0]][current[1]])
    #     return shortest_path(pred[current[0]][current[1]], target, pred, path)
    # shortest_path([0, 0], [len(data)-1, len(data[0])-1], pred)
    # print()
    return dist[len(data)-1][len(data[0])-1]

def repeat_map(_map):
    new_map = [[0 for _ in range(5*len(_map[0]))] for _ in range(5*len(_map))]

    n, m = len(_map), len(_map[0])

    for i in range(len(new_map)):
        for j in range(len(new_map)):
            new_map[i][j] = ((_map[i % n][j % m] + i // n + j // m) - 1) % 9 + 1
            # if i < len(_map) and j < len(_map[0]):
            #     new_map[i][j] = _map[i][j]
            #     continue
            # newi = (i // n - 1) * n + (i % n)
            # newj = (j // m - 1) * m + (j % m)
            # # newi = i - len(_map)
            # # newj = j - len(_map[0])

            # if newi < 0:
            #     newi = i
            # if newj < 0:
            #     newj = j

            # print(i, j, newi, newj)
            # if newi > len(_map) and newj > len(_map[0]):
            #     new_map[i][j] = new_map[newi][newj] + 1
            # else:
            #     new_map[i][j] = new_map[newi][newj] + 1
            # print(i, j, i - len(_map), j - len(_map[0]))
            # if i > len(_map) and j > len(_map[0]):
            #     new_map[i][j] = _map[i - len(_map)][j  len(_map[0])] + 1
            # elif j > len(_map[0]):
            #     new_map[i][j] = _map[i][j - len(_map[0])] + 1
            # elif i > len(_map):
            #     new_map[i][j] = _map[i - len(_map)][j] + 1
            
            # if new_map[i][j] > 9:
            #     new_map[i][j] = 1
    return new_map

def solve_p2(raw_data):
    data = process_input(raw_data)
    print(len(data), len(data))
    data = repeat_map(data)

    pq = PriorityQueue()
    pq.put((0, [0, 0]))

    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    result = 0

    while not pq.empty():
        (risc, cur) = pq.get()

        if visited[cur[0]][cur[1]]:
            continue

        if cur[0] == len(data)-1 and cur[1] == len(data[0])-1:
            result = risc
            break

        visited[cur[0]][cur[1]] = 1

        y, x = cur

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx >= len(data[0]) or nx < 0:
                continue
            if ny >= len(data) or ny < 0:
                continue
            if visited[ny][nx]:
                continue
            pq.put((risc + data[ny][nx], [ny, nx]))

    return result