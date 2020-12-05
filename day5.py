import util
import math


def first(input_path: str):
    seat_ids = []
    with open(input_path) as file:
        lines = file.read().splitlines()
    for line in lines:
        c = 0
        row_low = 0
        row_high = 127
        while c < 7:
            mid = math.floor((row_low + row_high) / 2)
            if line[c] == 'F':
                row_high = mid
            elif line[c] == 'B':
                row_low = mid+1
            c += 1
        col_low = 0
        col_high = 7
        while c < 10:
            mid = math.floor((col_low + col_high) / 2)
            if line[c] == 'L':
                col_high = mid
            elif line[c] == 'R':
                col_low = mid+1
            c += 1
        seat_ids.append(row_high * 8 + col_high)
    print(f'Result: {max(seat_ids)}')


def second(input_path: str):
    seat_ids = []
    with open(input_path) as file:
        lines = file.read().splitlines()
    for line in lines:
        c = 0
        row_low = 0
        row_high = 127
        while c < 7:
            mid = math.floor((row_low + row_high) / 2)
            if line[c] == 'F':
                row_high = mid
            elif line[c] == 'B':
                row_low = mid+1
            c += 1
        col_low = 0
        col_high = 7
        while c < 10:
            mid = math.floor((col_low + col_high) / 2)
            if line[c] == 'L':
                col_high = mid
            elif line[c] == 'R':
                col_low = mid+1
            c += 1
        seat_ids.append(row_high * 8 + col_high)
    for seat in range(0, 127 * 8 + 7):
        if seat  not in seat_ids:
            if seat+1 in seat_ids and seat-1 in seat_ids:
                print(f'Result: {seat}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
    if util.file_exists(path):
        second(path)
