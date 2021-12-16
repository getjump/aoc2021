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
    return ''.join([bin(int(x, 16))[2:].zfill(4) for x in raw_data.split('\n')[0]])

def bin2dec(data):
    return int(data, 2)

def parse_packet(packet_data, nl=0):
    if packet_data == '':
        return 0, '0'

    version = packet_data[:3]
    typeId = packet_data[3:6]

    sep = '    ' * nl

    # print(sep, packet_data)
    # print(sep, 'version', bin2dec(version), 'typeId', bin2dec(typeId))

    version_sum = int(bin2dec(version))

    length = 6
    decimal = None

    if bin2dec(typeId) != 4:
        ops = {'0': np.sum, '1': np.product, '2': np.min, '3': np.max, '5': lambda x: int(x[0] > x[1]), '6': lambda x: int(x[0] < x[1]), '7': lambda x: int(x[0] == x[1])}

        OPERATION = ops[str(bin2dec(typeId))]
        OPERANDS = []

        lengthTypeId = packet_data[6]
        length += 1
        # print('lentypeid', lengthTypeId)
        if lengthTypeId == '0':
            totalLengthSubp = bin2dec(packet_data[7:22])
            # print(sep, totalLengthSubp, 'length subp', packet_data[7:22])
            length += totalLengthSubp + 15
            start = 22
            while start < 22 + totalLengthSubp:
                l, v, d = parse_packet(packet_data[start:22+totalLengthSubp], nl+1)
                if d is not None:
                    OPERANDS.append(d)
                version_sum += int(v)
                # while l % 4 != 0:
                    # l += 1
                start += l
                # if l == 0:
                    # break
                # print('' * nl + 'start', 'l', start, l)
                # break
                # if start > 33:
                    # break
        elif lengthTypeId == '1':
            numberOfSubp = bin2dec(packet_data[7:18])
            # print(sep, 'num_subp', numberOfSubp, packet_data[7:18])
            length += 11
            start = 18
            while numberOfSubp > 0:
                packet_length, v, d = parse_packet(packet_data[start:], nl+1)
                if d is not None:
                    OPERANDS.append(d)
                # print(sep, packet_data[start:], packet_length)
                version_sum += int(v)
                # print(packet_length, 'subp lenth')
                length += packet_length
                start += packet_length
                numberOfSubp -= 1

        decimal = OPERATION(OPERANDS)

        return length, version_sum, decimal
    elif bin2dec(typeId) == 4:
        start = 6
        chunks = []
        while packet_data[start] == '1':
            chunks.append(packet_data[start+1:start+5])
            start += 5
            length += 5
        chunks.append(packet_data[start+1:start+5])
        # print(sep, ''.join(chunks))
        # print(sep, 'decimal', bin2dec(''.join(chunks)))
        decimal = bin2dec(''.join(chunks))
        length += 5
        # nested packages
    # print(sep, 'version_sum', version_sum)

    return length, version_sum, decimal

def solve_p1(raw_data):    
    data = process_input(raw_data)
    _, sum, _ = parse_packet(data)
    return sum

def solve_p2(raw_data):
    data = process_input(raw_data)
    _, _, v = parse_packet(data)
    return v
