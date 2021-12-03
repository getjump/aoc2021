from functools import reduce
import numpy as np

def find_cbc(data):
    cbc = [[0, 0] for _ in range(0, len(data[0]))]

    for l in data:
        for c in range(0, len(l)):
            cbc[c][int(l[c])] += 1

    return cbc

def solve_p1(raw_data):
    data = list(raw_data.split('\n'))

    cbc = [[0, 0] for _ in range(0, len(data[0]))]

    for l in data:
        for c in range(0, len(l)):
            cbc[c][int(l[c])] += 1

    gamma_rate, epsilon_rate = "", ""

    for x in cbc:
        if x[0] > x[1]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def solve_p2(raw_data):
    data = list(raw_data.split('\n'))

    ox_rating = 0
    co2_rating = 0

    ox_numbers = [l for l in data]
    co2_numbers = [l for l in data]

    bit = 0

    while len(ox_numbers) > 1:
        cbc = find_cbc(ox_numbers)
        new_ox_numbers = []
        if cbc[bit][0] > cbc[bit][1]:
            for n in ox_numbers:
                if n[bit] == "0":
                    new_ox_numbers.append(n)
        elif cbc[bit][0] < cbc[bit][1]:
            for n in ox_numbers:
                if n[bit] == "1":
                    new_ox_numbers.append(n)
        else:
            for n in ox_numbers:
                if n[bit] == "1":
                    new_ox_numbers.append(n)
        bit += 1
        ox_numbers = new_ox_numbers

    bit = 0

    while len(co2_numbers) > 1:
        cbc = find_cbc(co2_numbers)
        new_co2_numbers = []
        if cbc[bit][0] > cbc[bit][1]:
            for n in co2_numbers:
                if n[bit] == "1":
                    new_co2_numbers.append(n)
        elif cbc[bit][0] < cbc[bit][1]:
            for n in co2_numbers:
                if n[bit] == "0":
                    new_co2_numbers.append(n)
        else:
            for n in co2_numbers:
                if n[bit] == "0":
                    new_co2_numbers.append(n)
        bit += 1
        co2_numbers = new_co2_numbers
    
    return int(co2_numbers[0], 2) * int(ox_numbers[0], 2)