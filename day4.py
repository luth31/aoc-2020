import util


def byr(in_str: str) -> bool:
    try:
        year = int(in_str)
        if 1920 <= year <= 2002:
            return True
    except ValueError:
        return False
    return False


def iyr(in_str: str) -> bool:
    try:
        year = int(in_str)
        if 2010 <= year <= 2020:
            return True
    except ValueError:
        return False
    return False


def eyr(in_str: str) -> bool:
    try:
        year = int(in_str)
        if 2010 <= year <= 2030:
            return True
    except ValueError:
        return False
    return False


def hgt(in_str: str) -> bool:
    try:
        height = int(in_str[:-2])
        if in_str[-2:] == 'cm':
            if 150 <= height <= 193:
                return True
        elif in_str[-2:] == 'in':
            if 59 <= height <= 76:
                return True
    except ValueError:
        return False
    return False


def hcl(in_str: str) -> bool:
    if len(in_str) != 7:
        return False
    if in_str[0] == '#':
        for c in in_str[1:]:
            if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
    return True


def ecl(in_str: str) -> bool:
    if in_str not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    return True


def pid(in_str: str) -> bool:
    if len(in_str) != 9:
        return False
    try:
        int(in_str)
    except ValueError:
        return False
    return True


def cid(in_str: str) -> bool:
    return True


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
handlers = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': cid
}


def first(input_path: str):
    valid_pass = 0
    with open(input_path) as file:
        lines = file.read().split('\n\n')
    for line in lines:
        line = line.split()
        keys = []
        for attr in line:
            kv = attr.split(':')
            keys.append(kv[0])
        if all(elem in keys for elem in fields):
            valid_pass += 1
    print(f'Valid passports: {valid_pass}')


def second(input_path: str):
    valid_pass = 0
    with open(input_path) as file:
        passports = file.read().split('\n\n')
    for passport in passports:
        passport = passport.split()
        keys = []
        for attr in passport:
            kv = attr.split(':')
            keys.append(kv[0])
        if all(elem in keys for elem in fields):
            valid = True
            for attr in passport:
                kv = attr.split(':')
                check = handlers.get(kv[0])
                if not check(kv[1]):
                    valid = False
            if valid:
                valid_pass += 1
    print(f'Valid passports: {valid_pass}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
    if util.file_exists(path):
        second(path)
