from functools import reduce
import numpy as np
import math
from itertools import permutations

from numpy.lib.arraysetops import intersect1d

def process_input(raw_data):
    return list(map(lambda x: x.split(' | '), raw_data.strip().split('\n')))

def solve_p1(raw_data):
    data = process_input(raw_data)

    numbers_segments = [[], [], [], [], [], [], [], [], [], []]

    segments_numbers = {
        'a': [0, 2, 3, 5, 6, 7, 8, 9],
        'b': [0, 4, 5, 6, 8, 9],
        'c': [0, 1, 2, 3, 4, 7, 8, 9],
        'd': [2, 3, 4, 5, 6, 8, 9],
        'e': [0, 2, 6, 8],
        'g': [0, 2, 3, 5, 6, 8, 9],
        'f': [0, 1, 3, 4, 5, 6, 7, 8, 9]
    }

    for key, val in segments_numbers.items():
        for d in val:
            numbers_segments[d].append(key)

    digits = []

    mapping = {x:[] for x in range(0, 10)}

    for segments in data:
        for segment in segments[1].split(' '):
            for i in range(len(numbers_segments)):
                result = []
                for char in segment:
                    result.append(char)
                if len(segment) == len(numbers_segments[i]):
                    if len(mapping[i]) == 0:
                        mapping[i] = result
                    else:
                        mapping[i] = np.intersect1d(mapping[i], result)
        inverse_mapping = {}
        
        for dig, vals in mapping.items():
            for char in vals:
                if char not in inverse_mapping:
                    inverse_mapping[char] = []
                inverse_mapping[char].append(dig)

    result = 0

    for i in digits:
        if i == 1:
            result += 1
        elif i == 4:
            result += 1
        elif i == 7:
            result += 1
        elif i == 8:
            result += 1
    return result

def solve_p2(raw_data):
    data = process_input(raw_data)

    numbers_segments = [[], [], [], [], [], [], [], [], [], []]

    segments_numbers = {
        'a': [0, 2, 3, 5, 6, 7, 8, 9],
        'b': [0, 4, 5, 6, 8, 9],
        'c': [0, 1, 2, 3, 4, 7, 8, 9],
        'd': [2, 3, 4, 5, 6, 8, 9],
        'e': [0, 2, 6, 8],
        'g': [0, 2, 3, 5, 6, 8, 9],
        'f': [0, 1, 3, 4, 5, 6, 7, 8, 9]
    }

    valid = [set(x) for x in ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]]

    def is_valid(translation):
        translated = set()
        for char in translation:
            translated.add(char)
        if not translated in valid:
            return False
        return True

    for key, val in segments_numbers.items():
        for d in val:
            numbers_segments[d].append(key)

    all_chars = ['a', 'b', 'c', 'd', 'e', 'g', 'f']

    sum = 0

    for segments in data:
        mapping = {x:[] for x in range(0, 10)}
        mapping_char = {x: [] for x in all_chars}

        segments_to_process = []
        for segment in segments[0].split(' '):
            if len(segment) == len(numbers_segments[1]):
                mapping[1] = [char for char in segment]
                for char in segment:
                    mapping_char[char].append(1)
                continue
            if len(segment) == len(numbers_segments[4]):
                mapping[4] = [char for char in segment]
                for char in segment:
                    mapping_char[char].append(4)
                continue
            if len(segment) == len(numbers_segments[7]):
                mapping[7] = [char for char in segment]
                for char in segment:
                    mapping_char[char].append(7)
                continue
            if len(segment) == len(numbers_segments[8]):
                mapping[8] = [char for char in segment]
                for char in segment:
                    mapping_char[char].append(8)
                continue
            segments_to_process.append(segment)

            # for i in range(len(mapping)):
            #     if i not in [1, 4, 7, 8]:
            #         mapping[i] = [char for char in segment]
        a = np.setdiff1d(mapping[7], mapping[1])

        eg = np.setdiff1d(mapping[8], mapping[4] + [a[0]])

        mapping[0] = np.concatenate((mapping[0], a))
        mapping[2] = np.concatenate((mapping[2], a))
        mapping[3] = np.concatenate((mapping[3], a))
        mapping[5] = np.concatenate((mapping[5], a))
        mapping[6] = np.concatenate((mapping[6], a))
        mapping[9] = np.concatenate((mapping[9], a))

        mapping[0] = np.concatenate((mapping[0], eg))
        mapping[2] = np.concatenate((mapping[2], eg))
        mapping[6] = np.concatenate((mapping[6], eg))

        mapping[0] = np.concatenate((mapping[0], mapping[7]))
        mapping[3] = np.concatenate((mapping[3], mapping[7]))
        mapping[9] = np.concatenate((mapping[9], mapping[7]))
        
        bd = np.setdiff1d([*mapping[4], *eg, *a], mapping[0])
        mapping[5] = np.concatenate((mapping[5], bd))
        mapping[6] = np.concatenate((mapping[6], bd))
        mapping[9] = np.concatenate((mapping[9], bd))
        
        cf = np.setdiff1d(mapping[4], bd)
        mapping[0] = np.concatenate((mapping[0], cf))
        mapping[3] = np.concatenate((mapping[3], cf))
        mapping[9] = np.concatenate((mapping[9], cf))

        for (b, d) in permutations(bd):
            for (e, g) in permutations(eg):
                for (c, f) in permutations(cf):
                    sum = 0

                    mapping_test = dict(mapping)

                    mapping_test[0] = np.concatenate((mapping_test[0], [b]))

                    mapping_test[2] = np.concatenate((mapping_test[2], [c]))

                    mapping_test[5] = np.concatenate((mapping_test[5], [f]))
                    mapping_test[6] = np.concatenate((mapping_test[6], [f]))
                        
                    mapping_test[2] = np.concatenate((mapping_test[2], [d]))
                    mapping_test[3] = np.concatenate((mapping_test[3], [d]))

                    mapping_test[3] = np.concatenate((mapping_test[3], [g]))
                    mapping_test[5] = np.concatenate((mapping_test[5], [g]))
                    mapping_test[9] = np.concatenate((mapping_test[9], [g]))

                    mapping_test[2] = np.concatenate((mapping_test[2], [e]))

                    for i in range(len(mapping_test)):
                        mapping_test[i] = np.unique(mapping_test[i])

                    inverse_mapping = {}

                    for i in range(len(mapping_test)):
                        for j in range(len(mapping_test[i])):
                            if mapping_test[i][j] not in inverse_mapping:
                                inverse_mapping[mapping_test[i][j]] = []
                            inverse_mapping[mapping_test[i][j]].append(i)
                    
                    # print(inverse_mapping)

                    digits = []
                    alphabet = {a[0]: 'a', b: 'b', c: 'c', d: 'd', e: 'e', f: 'f', g: 'g'}
                    # print(alphabet)

                    break_condition = False
                    count_true = 0

                    for segment in segments[1].split(' '):
                        translation = [alphabet[char] for char in segment]
                        
                        if not is_valid(translation):
                            break_condition = True
                            break
                        count_true += 1
                        # print('translation', translation, is_valid(translation))
                        result = []
                        if len(segment) == len(numbers_segments[1]):
                            digits.append(1)
                            continue
                        if len(segment) == len(numbers_segments[4]):
                            digits.append(4)
                            continue
                        if len(segment) == len(numbers_segments[7]):
                            digits.append(7)
                            continue
                        if len(segment) == len(numbers_segments[8]):
                            digits.append(8)
                            continue

                        for char in segment:
                            if len(result) == 0:
                                result = inverse_mapping[char]
                            else:
                                # print(char, result)
                                result = np.intersect1d(result, inverse_mapping[char])
                        
                        # print(result, segment)
                        if len(result) > 1:
                            for i in result:
                                if i != 8 and i != 1 and i != 4 and i != 7:
                                    digits.append(i)
                                    break
                        elif len(result) == 1:
                            digits.append(result[0])
                    
                    # print(break_condition)
                    if break_condition:
                        continue
                    
                    print('dig', [str(x) for x in digits], count_true)
                    sum += int(str(''.join([str(x) for x in digits])))
                    print('sum', sum)
                    # return
        # print(segment, digits)

    return sum