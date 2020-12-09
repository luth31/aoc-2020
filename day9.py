import util


def is_in_data(data: list, value: int):
    for i in data:
        for j in data:
            if i + j == value:
                return True
    return False


def first(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    numbers = [int(x) for x in lines]
    preamble = 25
    data = []
    for i in range(0, preamble):
        data.append(numbers[i])
    i = 0
    for number in numbers[preamble:]:
        if i == preamble:
            i = 0
        if not is_in_data(data, number):
            print(f'Found invalid number: {number}')
            return
        else:
            data[i] = number
            i += 1


def second(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    numbers = [int(x) for x in lines]
    preamble = 25
    data = []
    weakness = 0
    for i in range(0, preamble):
        data.append(numbers[i])
    i = 0
    for number in numbers[preamble:]:
        if i == preamble:
            i = 0
        if not is_in_data(data, number):
            weakness = number
            break
        else:
            data[i] = number
            i += 1
    for start in range(0, len(lines)-2):
        for end in range(start+2, len(lines)):
            total = 0
            min_val = numbers[start]
            max_val = numbers[start]
            for it in range(start, end+1):
                if numbers[it] < min_val:
                    min_val = numbers[it]
                if numbers[it] > max_val:
                    max_val = numbers[it]
                total += numbers[it]
            if total == weakness:
                print(f'Found weakness: {min_val + max_val}')
                return


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
