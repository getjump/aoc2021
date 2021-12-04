from functools import reduce
import numpy as np

def solve_p1(raw_data):
    data = list(raw_data.split('\n'))

    numbers = map(int, data[0].split(','))
    
    board_data = []

    for x in data[2:]:
        if x.strip() == '':
            continue
        _d = []
        for n in x.strip().split(' '):
            if n != '':
                _d.append(int(n))
    
        board_data.append(_d)

    boards = []

    for i in range(0, int(len(board_data)/5)):
        boards.append([[y for y in x] for x in board_data[i*5:i*5+5]])

    lastScore = 0

    for n in numbers:
        score = 0
        for b in boards:
            for i in range(0, 5):
                for j in range(0, 5):
                    if b[i][j] == n:
                        b[i][j] = -1
            
            row_win_cond = False
            
            for i in range(0, 5):
                row_win_count = 0
                for j in range(0, 5):
                    if b[i][j] == -1:
                        row_win_count += 1
                if row_win_count >= 5:
                    row_win_cond = True
            
            col_win_cond = False
            for i in range(0, 5):
                col_win_count = 0
                for j in range(0, 5):
                    if b[j][i] == -1:
                        col_win_count += 1
                if col_win_count >= 5:
                    col_win_cond = True

            

            if col_win_cond or row_win_cond:
                for i in range(0, 5):
                    for j in range(0, 5):
                        if b[i][j] != -1:
                            score += b[i][j]

        score *= int(n)
        if score > 0:
            return score

def solve_p2(raw_data):
    data = list(raw_data.split('\n'))

    numbers = map(int, data[0].split(','))
    
    board_data = []

    for x in data[2:]:
        if x.strip() == '':
            continue
        _d = []
        for n in x.strip().split(' '):
            if n != '':
                _d.append(int(n))
    
        board_data.append(_d)

    boards = []

    for i in range(0, int(len(board_data)/5)):
        boards.append([[y for y in x] for x in board_data[i*5:i*5+5]])

    lastScore = 0

    for n in numbers:
        score = 0
        bi = 0
        while bi < len(boards):
            b = boards[bi]
            for i in range(0, 5):
                for j in range(0, 5):
                    if b[i][j] == n:
                        b[i][j] = -1
            
            row_win_cond = False
            
            for i in range(0, 5):
                row_win_count = 0
                for j in range(0, 5):
                    if b[i][j] == -1:
                        row_win_count += 1
                if row_win_count >= 5:
                    row_win_cond = True
            
            col_win_cond = False
            for i in range(0, 5):
                col_win_count = 0
                for j in range(0, 5):
                    if b[j][i] == -1:
                        col_win_count += 1
                if col_win_count >= 5:
                    col_win_cond = True

            if col_win_cond or row_win_cond:
                del boards[bi]
                for i in range(0, 5):
                    for j in range(0, 5):
                        if b[i][j] != -1:
                            score += b[i][j]
            else:
                bi += 1

        score *= int(n)
        if score > 0:
            lastScore = score
        bi += 1
    
    return lastScore