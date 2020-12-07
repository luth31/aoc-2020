import util

bags = []


class Bag:
    def __init__(self, name: str) -> None:
        self.name = name
        self.sub_bags = []
        bags.append(self)

    def add_sub_bag(self, sb: 'Bag', count: int) -> None:
        self.sub_bags.append((sb, count))


def get_bag(name: str) -> Bag:
    for bag in bags:
        if bag.name == name:
            return bag
    bag = Bag(name)
    return bag


def parse_rule(rule: str) -> None:
    rule = rule.split(' ')
    bag_name = rule[0] + ' ' + rule[1]
    bag = get_bag(bag_name)
    if rule[4] == 'no':
        return
    i = 4
    while i < len(rule):
        sb_count = rule[i]
        sb_name = rule[i+1] + ' ' + rule[i+2]
        sb = get_bag(sb_name)
        bag.add_sub_bag(sb, int(sb_count))
        i += 4


def count_root_bags_for(bag_name: str) -> int:
    resolvee = get_bag(bag_name)
    total = 0
    for bag in bags:
        visited = []
        queue = []
        found = False
        visited.append(bag)
        queue.append(bag)
        while queue:
            it_bag = queue.pop(0)
            for sb, _ in it_bag.sub_bags:
                if sb == resolvee:
                    found = True
                    break
                if sb not in visited:
                    visited.append(sb)
                    queue.append(sb)
            if found:
                total += 1
                break
    return total


def count_bags_for(bag_name: str) -> int:
    total = 0
    resolvee = get_bag(bag_name)
    if len(resolvee.sub_bags) == 0:
        return 1
    for bag, count in resolvee.sub_bags:
        total += count * count_bags_for(bag.name)
    return total + 1


def first(input_path: str) -> None:
    with open(input_path) as file:
        lines = file.read().split('\n')
    for line in lines:
        parse_rule(line)
    result = count_root_bags_for('shiny gold')
    print(f'The answer is: {result}')


def second() -> None:
    result = count_bags_for('shiny gold') - 1
    print(f'The answer is: {result}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second()
