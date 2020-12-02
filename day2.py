import util


def first(input_path: str):
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
    (first_path, second_path) = util.get_input_paths(__file__)
    if util.file_exists(first_path):
        first(first_path)
    if util.file_exists(second_path):
        second(second_path)
