from functools import reduce
import numpy as np

def solve_p1(raw_data):
    data = list(raw_data.split('\n'))

    pos = 0
    depth = 0

    for cmd in data:
        cmds, val = cmd.split(' ')
        val = int(val)

        if cmds == 'forward':
            pos += val
        if cmds == 'down':
            depth += val
        if cmds == 'up':
            depth -= val

    return pos * depth

def solve_p2(raw_data):
    data = list(raw_data.split('\n'))

    pos = 0
    depth = 0
    aim = 0

    for cmd in data:
        cmds, val = cmd.split(' ')
        val = int(val)

        if cmds == 'forward':
            pos += val
            if aim != 0:
                depth += aim * val
        if cmds == 'down':
            aim += val
        if cmds == 'up':
            aim -= val

    return pos * depth