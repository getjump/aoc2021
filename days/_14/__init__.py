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

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    data= raw_data.split('\n')
    return data[0], list(map(lambda x: x.split(' -> '), data[2:]))

def solve_p1(raw_data):    
    str, data = process_input(raw_data)
    new_str = copy.deepcopy(str)

    return

    for step in range(10):
        mapper = {x: x for x in range(len(str))}
        for replace, w in data:
            for i in range(1, len(str)):
                if str[i-1] + str[i] == replace:
                    # print(str[i-1], str[i], i, j, new_str[0:i+j], w, new_str[i+j:])
                    new_str = new_str[0:mapper[i]] + w + new_str[mapper[i]:]
                    for c in range(i, len(str)):
                        mapper[c] += 1
        str = ''.join(new_str)
        print(len(str), step, str)

    counters = defaultdict(int)

    for i in str:
        counters[i] += 1
    
    print(counters)
    counters = sorted(counters.values())
    return counters[-1] - counters[0]

def solve_p2(raw_data):
    str, data = process_input(raw_data)
    new_str = copy.deepcopy(str)

    mappings = {}

    for replace, w in data:
        mappings[replace] = w

    counters = defaultdict(int)

    for i in range(1, len(str)):
        counters[str[i-1] + str[i]] += 1
    
    for step in range(40):
        new_counters = defaultdict(int)
        for replace in counters:
            transform = mappings[replace]
            
            new_counters[replace[0] + transform] += counters[replace]
            new_counters[transform + replace[1]] += counters[replace]
        counters = new_counters
    
    fc = defaultdict(int)
    sc = defaultdict(int)

    print(counters)

    for p in counters:
        fc[p[0]] += counters[p]
        sc[p[1]] += counters[p]

    print(fc)
    print(sc)

    c = {x: max(fc[x], sc[x]) for x in set(fc)}
    print(c)

    return max(c.values()) - min(c.values())