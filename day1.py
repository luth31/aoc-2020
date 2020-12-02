import os.path
import sys


def file_exists(path: str):
    if not os.path.isfile(path):
        print(f'Error: File {path} not found or not a file!')
        return False
    return True


def first(input_path: str):
    pass


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
