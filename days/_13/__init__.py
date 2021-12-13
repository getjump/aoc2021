from functools import reduce
from typing import DefaultDict
import numpy as np
import math
from itertools import permutations
import copy
from collections import defaultdict
from numpy.core.fromnumeric import resize

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return [x.split(',') for x in raw_data.strip().split('\n')]

def foldx(x, paper):
    new_paper = [[0 for _ in range(x)] for _ in range(len(paper))]
    print(np.array(paper))
    for i in range(len(paper)):
        for j in range(x):
            new_paper[i][j] = paper[i][j] + paper[i][2*x - j]
    
    return new_paper

def foldy(y, paper):
    new_paper = [[0 for _ in range(len(paper[0]))] for _ in range(y)]

    for i in range(y):
        for j in range(len(paper[i])):
            new_paper[i][j] = paper[i][j] + paper[2*y - i][j]
    
    return new_paper

def solve_p1(raw_data):
    data = process_input(raw_data)
    
    points = []
    folds = []

    maxx, maxy = 0, 0

    for stuff in data:
        if len(stuff) >= 2:
            points.append(list(map(int, stuff)))
            if points[-1][0] > maxx:
                maxx = points[-1][0]
            if points[-1][1] > maxy:
                maxy = points[-1][1]
        elif 'fold' in stuff[0]:
            folds.append(stuff[0])
    
    paper = [[0 for _ in range(maxx+1)] for _ in range(maxy+1)]
    for p in points:
        print(p)
        paper[p[1]][p[0]] = 1

    print(np.array(paper))

    coord_to_f = {'x': foldx, 'y': foldy}

    new_paper = copy.deepcopy(paper)

    for f in folds:
        fold = coord_to_f[f[11]]
        val = int(f[13:])
        new_paper = fold(val, new_paper)
        break

    result = 0
    for i in range(len(new_paper)):
        for j in range(len(new_paper[0])):
            if new_paper[i][j] > 0:
                result += 1
    return result

def solve_p2(raw_data):
    data = process_input(raw_data)
    
    points = []
    folds = []

    maxx, maxy = 0, 0

    for stuff in data:
        if len(stuff) >= 2:
            points.append(list(map(int, stuff)))
            if points[-1][0] > maxx:
                maxx = points[-1][0]
            if points[-1][1] > maxy:
                maxy = points[-1][1]
        elif 'fold' in stuff[0]:
            folds.append(stuff[0])
    
    paper = [[0 for _ in range(maxx+1)] for _ in range(maxy+1)]
    for p in points:
        print(p)
        paper[p[1]][p[0]] = 1

    print(np.array(paper))

    coord_to_f = {'x': foldx, 'y': foldy}

    new_paper = copy.deepcopy(paper)

    for f in folds:
        fold = coord_to_f[f[11]]
        val = int(f[13:])
        new_paper = fold(val, new_paper)
        print_paper(new_paper)

    result = 0
    for i in range(len(new_paper)):
        for j in range(len(new_paper[0])):
            if new_paper[i][j] > 0:
                result += 1
    return result

def print_paper(paper):
    result = ''
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] > 0:
                result += '#'
            else:
                result += '.'
        result += "\n"
    print(result)