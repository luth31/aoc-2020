import util


dir_map = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}


def normalize_degrees(degrees: int) -> int:
    if degrees < 0:
        degrees = 360 + degrees
    elif degrees >= 360:
        degrees -= 360
    return degrees


def do_action(action: str, value: int, direction: int, distances: map):
    if action in ['N', 'S', 'W', 'E']:
        distances[action] += value
    elif action == 'F':
        distances[dir_map[direction]] += value
    elif action == 'R':
        direction += value
    elif action == 'L':
        direction -= value
    return normalize_degrees(direction)


def do_action2(action: str, value: int, distances: map, waypoint: map):
    if action in ['N', 'S', 'W', 'E']:
        waypoint[action] += value
    elif action == 'F':
        for key in distances.keys():
            distances[key] += waypoint[key] * value
    elif action == 'R':
        rotations = int(normalize_degrees(value) / 90)
        for i in range(rotations):
            temp = waypoint['W']
            waypoint['W'] = waypoint['S']
            waypoint['S'] = waypoint['E']
            waypoint['E'] = waypoint['N']
            waypoint['N'] = temp
    elif action == 'L':
        rotations = int(normalize_degrees(value) / 90)
        for i in range(rotations):
            temp = waypoint['N']
            waypoint['N'] = waypoint['E']
            waypoint['E'] = waypoint['S']
            waypoint['S'] = waypoint['W']
            waypoint['W'] = temp


def first(input_path: str) -> None:
    distances = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = []
    for line in lines:
        data.append((line[0], int(line[1:])))
    direction = 90
    for (action, value) in data:
        direction = do_action(action, value, direction, distances)
    total = abs(distances['N'] - distances['S']) + abs(distances['W'] - distances['E'])
    print(f'First: {total}')


def second(input_path: str) -> None:
    waypoint = {'N': 1, 'S': 0, 'W': 0, 'E': 10}
    distances = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    with open(input_path) as file:
        lines = file.read().split('\n')
    data = []
    for line in lines:
        data.append((line[0], int(line[1:])))
    for (action, value) in data:
        do_action2(action, value, distances, waypoint)
    total = abs(distances['N'] - distances['S']) + abs(distances['W'] - distances['E'])
    print(f'First: {total}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
