from argparse import ArgumentParser
import argparse
import days
import os
import importlib
import glob

parser = argparse.ArgumentParser()

maxDay = 0

for day in glob.glob('./days/*'):
    day = os.path.basename(os.path.normpath(day))
    if day == '__init__.py' or day == '__pycache__':
        continue
    if int(day[1:]) > maxDay:
        maxDay = int(day[1:])

parser.add_argument('day', metavar='day', type=int, nargs='?', help='specifies day to solve')
parser.add_argument('--ignore-actual', dest='ignoreActual', action='store_true', default=False, help='ignore actual')

args = parser.parse_args()

if args.day is not None:
    day = args.day
else:
    day = str(maxDay)

day_dir = f'days/_{day}'

if not os.path.isdir(day_dir):
    print(f'directory {day_dir} doesn\'t exists')
    exit(0)

test_input_file = f'{day_dir}/test_input.txt'

input_file = f'{day_dir}/input.txt'

if not os.path.isfile(input_file):
    print(f'Test input doesn\'t exists')
    exit(0)

f = open(input_file)
raw_data = f.read().rstrip()

alias = importlib.import_module(day_dir.replace('/', '.'))

print(f'Solving day {day}')

if os.path.isfile(test_input_file):
    f_test_input_file = open(test_input_file)
    ans_p1, ans_p2 = map(str.strip, f_test_input_file.readline().strip().split(','))
    raw_test_input_data = f_test_input_file.read()

    solved_p1, solved_p2 = alias.solve_p1(raw_test_input_data), alias.solve_p2(raw_test_input_data)
    print('Test input:', f'p1={solved_p1}', '==', ans_p1, str(solved_p1) == ans_p1, f'p2={solved_p2}', '==', ans_p2, str(solved_p2) == ans_p2)

if not args.ignoreActual:
    print('Actual output:', f'p1={alias.solve_p1(raw_data)}', f'p2={alias.solve_p2(raw_data)}')