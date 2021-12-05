from functools import reduce
import numpy as np

def solve_p1(raw_data):
    data = list(raw_data.split('\n'))

    intersections = [[0 for x in range(1000)] for y in range(1000)] 

    maxx, maxy = 0, 0

    for s in data:
        (x1, y1), (x2, y2) = list(map(lambda x: x.strip().split(','), s.strip().split('->')))
        (x1, y1) = int(x1), int(y1)
        (x2, y2) = int(x2), int(y2)

        maxx = max(x1, x2, maxx)
        maxy = max(y1, y2, maxy)

        if x1 != x2 and y1 != y2:
            continue

        if y1 != y2 and x1 != x2:
            continue

        if x1 > x2:
            x1, x2 = x2, x1
        
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                intersections[i][j] += 1

    result = 0
    for i in range(0, maxx+1):
        for j in range(0, maxy+1):
            if intersections[i][j] > 1:
                result += 1

    return result

def solve_p2(raw_data):
    data = list(raw_data.split('\n'))

    intersections = [[0 for x in range(1000)] for y in range(1000)] 

    maxx, maxy = 0, 0

    for s in data:
        (x1, y1), (x2, y2) = list(map(lambda x: x.strip().split(','), s.strip().split('->')))
        (x1, y1) = int(x1), int(y1)
        (x2, y2) = int(x2), int(y2)

        maxx = max(x1, x2, maxx)
        maxy = max(y1, y2, maxy)

        if (x1 != x2 and y1 != y2):
            # diagonal
            # 1 3 -> 3 3
            # 1 1 2 2 3 3
            # 9 7 8 8 7 9
            # 8 0 7 1 6 2 5 3 4 4 3 5 2 6 1 7 0 8

            # for i in 
            # print((x1, y1), (x2, y2))
            dir = (1 if x1 < x2 else -1, 1 if y1 < y2 else -1)
            # print(dir)
            i = x1
            j = y1
            while i != x2+dir[0] and j != y2+dir[1]:
                # print(i, j)
                intersections[j][i] += 1
                i += dir[0]
                j += dir[1]
            # print_map(intersections, maxx, maxy)
            # print('')
            # break
            # for x in range(min(x1, x2, y1, y2), max(x1, x2, y1, y2)+1):
            #     intersections[i+x][j+x] += 1
            continue

        if x1 > x2:
            x1, x2 = x2, x1
        
        if y1 > y2:
            y1, y2 = y2, y1
        # print(x1, y1, x2, y2)
        
        if (x1 == x2 or y1 == y2):
            # horizontal or vertical
            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    intersections[i][j] += 1

    result = 0
    for i in range(0, maxx+1):
        _map = ''
        for j in range(0, maxy+1):
            if int(intersections[i][j]) >= 2:
                result += 1
            if intersections[i][j] == 0:
                _map += '.'
            else:
                _map += str(intersections[i][j])
        # print(_map)

    return result

def print_map(map, maxx, maxy):
    for i in range(0, maxx+1):
        _map = ''
        for j in range(0, maxy+1):
            if map[i][j] == 0:
                _map += '.'
            else:
                _map += str(map[i][j])
        print(_map)