import os.path
import sys


def file_exists(path: str):
    if not os.path.isfile(path):
        print(f'Error: File {path} not found or not a file!')
        return False
    return True


def first(input_path: str):
    lines = []
    passwords = 0
    with open(input_path) as file:
        lines = file.read().splitlines()
    for line in lines:
        split = line.split()
        (min_count_str, max_count_str) = split[0].split('-')
        min_count = int(min_count_str)
        max_count = int(max_count_str)
        char = split[1][:-1]
        password = split[2]
        char_count = password.count(char)
        if min_count <= char_count <= max_count:
            passwords += 1
    print(f"Valid passwords: {passwords}")


def second(input_path: str):
    lines = []
    passwords = 0
    with open(input_path) as file:
        lines = file.read().splitlines()
    for line in lines:
        split = line.split()
        (first_pos_str, second_pos_str) = split[0].split('-')
        first_pos = int(first_pos_str)
        second_pos = int(second_pos_str)
        char = split[1][:-1]
        password = split[2]
        if password[first_pos-1] == char or password[second_pos-1] == char:
            if password[first_pos-1] != password[second_pos-1]:
                passwords += 1
    print(f"Valid passwords: {passwords}")


if __name__ == '__main__':
    file_name = os.path.basename(__file__)[:-3]
    first_input = os.path.abspath(f'input/{file_name}_1.in')
    second_input = os.path.abspath(f'input/{file_name}_2.in')
    if file_exists(first_input):
        first(first_input)
    if file_exists(second_input):
        second(second_input)
