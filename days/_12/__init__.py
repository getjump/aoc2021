from functools import reduce
from typing import DefaultDict
import numpy as np
import math
from itertools import permutations
from graph_tool import *
import graph_tool.topology as gtt
import graph_tool.search as gts
import copy
from collections import defaultdict

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return [x.split('-') for x in raw_data.strip().split('\n')]

def build_graph(raw_data):
    data = process_input(raw_data)

    vertices = {}
    G = Graph(directed=False)

    name = G.new_vertex_property("string")

    for edge in data:
        (u, v) = edge
        if u not in vertices:
            vertices[u] = G.add_vertex()
            name[vertices[u]] = u

        if v not in vertices:
            vertices[v] = G.add_vertex()
            name[vertices[v]] = v
        
        G.add_edge(vertices[u], vertices[v])
    return G, name, vertices

def solve_p1(raw_data):
    G, name, vertices = build_graph(raw_data)
    used = G.new_vertex_property("bool")

    for v in G.vertices():
        used[v] = False

    paths = []

    def DFS(G, source, target, name, path=[]):
        path = path + [source]
        # print([name[x] for x in path])
        if source == target:
            paths.append(path)
        
        for e in source.out_edges():
            v = e.target()
            if not name[v].isupper() and v in path:
                continue
            DFS(G, v, target, name, path)

    DFS(G, vertices['start'], vertices['end'], name, [])

    return len(paths)

def solve_p2(raw_data):
    G, name, vertices = build_graph(raw_data)

    paths = []

    def DFS(G, source, target, name, path=[]):
        path = path + [source]
        small_cave_counter = defaultdict(int)
        for x in path:
            if name[x].islower() and (name[x] != 'start' or name[x] != 'end'):
                small_cave_counter[x] += 1

        twice_small_cave = False
        twice_small_cave_p = None
        for p, v in small_cave_counter.items():
            if twice_small_cave and p != twice_small_cave_p and v >= 2:
                return
            if v >= 2:
                twice_small_cave = True
                twice_small_cave_p = p

        # print([name[x] for x in path])
        if path.count(vertices['start']) > 1:
            return
        if source == target:
            paths.append(path)
            return
        
        for e in source.out_edges():
            v = e.target()
            if not name[v].isupper() and path.count(v) >= 2:
                continue
            DFS(G, v, target, name, path)

    DFS(G, vertices['start'], vertices['end'], name)

    return len(paths)