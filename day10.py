import util
import functools


def first(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = [int(x) for x in lines]
    data.append(0)
    data.sort()
    diffs = {1: 0, 2: 0, 3: 1}
    for idx in range(len(data) - 1):
        diffs[data[idx + 1] - data[idx]] += 1
    print(f'Answer: {diffs[1] * diffs[3]}')


@functools.cache
def walk(data, prev, end):
    if prev == end:
        return 1
    ways = 0
    for x in data:
        if 0 < x - prev <= 3:
            ways += walk(data, x, end)
    return ways


def second(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = [int(x) for x in lines]
    data.sort()
    data.append(data[-1]+3)
    ans = walk(tuple(data), 0, data[-1])
    print(f'Answer: {ans}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
