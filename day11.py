import util
import copy
from typing import Callable


def apply_rule2_for(old_data: list, data: list, x: int, y: int) -> None:
    if old_data[x][y] == '.':
        return
    total_adj = 0
    direction = [(- 1, - 1), (- 1, 0), (- 1, 1), (0, 1), (0, - 1), (1, - 1), (1, 0), (1, 1)]
    for (d_x, d_y) in direction:
        n_x = x
        n_y = y
        while True:
            n_x += d_x
            n_y += d_y
            if is_valid(old_data, n_x, n_y):
                if old_data[n_x][n_y] != '.':
                    if old_data[n_x][n_y] == '#':
                        total_adj += 1
                    break
            else:
                break
    if total_adj == 0:
        data[x][y] = '#'
    elif total_adj >= 5:
        data[x][y] = 'L'


def apply_rule_for(old_data: list, data: list, x: int, y: int) -> None:
    if old_data[x][y] == '.':
        return
    adjacent = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                (x + 1, y + 1)]
    total_adj = 0
    for (a_x, a_y) in adjacent:
        if is_valid(old_data, a_x, a_y):
            if old_data[a_x][a_y] == '#':
                total_adj += 1
    if total_adj == 0:
        data[x][y] = '#'
    elif total_adj >= 4:
        data[x][y] = 'L'


def lists_are_equal(list_a: list, list_b: list) -> bool:
    if len(list_a) != len(list_b):
        return False
    for x in range(len(list_a)):
        if len(list_a[x]) != len(list_b[x]):
            return False
        for y in range(len(list_a[x])):
            if list_a[x][y] != list_b[x][y]:
                return False
    return True


def do_run(data: list, snapshot: list, func: Callable[[list, list, int, int], None]) -> None:
    for x in range(len(data)):
        for y in range(len(data[x])):
            func(snapshot, data, x, y)


def count_occupied_seats(data: list) -> int:
    total = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == '#':
                total += 1
    return total


def is_valid(data: list, x: int, y: int) -> bool:
    if 0 <= x < len(data) and 0 <= y < len(data[x]):
        return True
    return False


def first(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = [[char for char in lines[i]] for i in range(len(lines))]
    snapshot = copy.deepcopy(data)
    while True:
        do_run(data, snapshot, apply_rule_for)
        if lists_are_equal(data, snapshot):
            break
        snapshot = copy.deepcopy(data)
    print(f'First: {count_occupied_seats(data)}')


def second(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = [[char for char in lines[i]] for i in range(len(lines))]
    snapshot = copy.deepcopy(data)
    while True:
        do_run(data, snapshot, apply_rule2_for)
        if lists_are_equal(data, snapshot):
            break
        snapshot = copy.deepcopy(data)
    print(f'Second: {count_occupied_seats(data)}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
