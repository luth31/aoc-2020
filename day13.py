import util
from sympy.ntheory.modular import crt


def first(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    arrival = int(lines[0])
    buses = [int(i) for i in lines[1].split(',') if i != 'x']
    min_dict = {}
    for bus in buses:
        time = bus
        i = 1
        while True:
            if time > arrival:
                min_dict[bus] = time - arrival
                break
            i += 1
            time += bus
    min_key = min(min_dict, key=min_dict.get)
    print(f'First: {min_key * min_dict[min_key]}')


def second(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    buses = [[int(i), -idx] for idx, i in enumerate(lines[1].split(',')) if i != 'x']
    bus = tuple(x[0] for x in buses)
    time = tuple(x[1] for x in buses)
    print(f'Second: {crt(bus, time)[0]}')


def second_slow(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    buses = [[int(i), idx] for idx, i in enumerate(lines[1].split(',')) if i != 'x']
    (h_key, h_val) = max(buses, key=lambda x: x[0])
    buses_off = [x for x in buses if x[0] != h_key]
    for bus in buses_off:
        bus[1] = bus[1] - h_val
    total = h_key
    while True:
        finish = True
        for bus in buses_off:
            if (total + bus[1]) % bus[0] != 0:
                finish = False
                break
        if finish:
            print(f'Second: {total - h_val}')
            return
        total += h_key


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
