import os.path
import sys


def file_exists(path: str):
    if not os.path.isfile(path):
        print(f'Error: File {path} not found or not a file!')
        return False
    return True


def first(input_path: str):
    numbers = []
    with open(input_path) as file:
        lines = file.read().splitlines()
        numbers = [int(i) for i in lines]
    for idx, i in enumerate(numbers[:-1]):
        for _, j in enumerate(numbers[idx+1:]):
            if i + j == 2020:
                print(f'The answer is: {i * j}')


def second(input_path: str):
    pass


if __name__ == '__main__':
    file_name = os.path.basename(__file__)[:-3]
    first_input = os.path.abspath(f'input/{file_name}_1.in')
    second_input = os.path.abspath(f'input/{file_name}_2.in')
    if file_exists(first_input):
        first(first_input)
    if file_exists(second_input):
        second(second_input)
