import util


def calc_with_slope(filepath: str, slope_x: int, slope_y: int):
    with open(filepath) as file:
        matrix = file.read().splitlines()
    trees = 0
    (x, y) = 0, 0
    while y < len(matrix)-1:
        x = (x + slope_x) % len(matrix[y])
        y += slope_y
        if matrix[y][x] == '#':
            trees += 1
    return trees


def first(input_path: str):
    print(f"Trees: {calc_with_slope(input_path, 3, 1)}")


def second(input_path: str):
    val = 1
    val *= calc_with_slope(input_path, 1, 1)
    val *= calc_with_slope(input_path, 3, 1)
    val *= calc_with_slope(input_path, 5, 1)
    val *= calc_with_slope(input_path, 7, 1)
    val *= calc_with_slope(input_path, 1, 2)
    print(f"Result: {val}")


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
    if util.file_exists(path):
        second(path)
