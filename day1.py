import util


def first(input_path: str):
    with open(input_path) as file:
        lines = file.read().splitlines()
        numbers = [int(i) for i in lines]
    for idx, i in enumerate(numbers[:-1]):
        for _, j in enumerate(numbers[idx+1:]):
            if i + j == 2020:
                print(f'The answer is: {i * j}')


def second(input_path: str):
    with open(input_path) as file:
        lines = file.read().splitlines()
        numbers = [int(i) for i in lines]
    for idx, i in enumerate(numbers[:-2]):
        for idy, j in enumerate(numbers[idx + 1:-1]):
            for idz, k in enumerate(numbers[idy + 1:]):
                if i + j + k == 2020:
                    print(f'The answer is: {i * j * k}. {idx} {idy} {idz}')


if __name__ == '__main__':
    (first_path, second_path) = util.get_input_paths(__file__)
    if util.file_exists(first_path):
        first(first_path)
    if util.file_exists(second_path):
        second(second_path)
