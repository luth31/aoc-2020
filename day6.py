import util


def first(input_path: str):
    total = 0
    with open(input_path) as file:
        groups = file.read().split('\n\n')
    for data in groups:
        answers = []
        group = data.split('\n')
        for person in group:
            for choice in person:
                if choice not in answers:
                    answers.append(choice)
        total += len(answers)
    print(f'Answer: {total}')


def second(input_path: str):
    total = 0
    with open(input_path) as file:
        groups = file.read().split('\n\n')
    for data in groups:
        answers = {}
        group = data.split('\n')
        for person in group:
            for choice in person:
                if choice not in answers:
                    answers[choice] = 1
                else:
                    answers[choice] += 1
        for _, v in answers.items():
            if v == len(group):
                total += 1
    print(f'Answer: {total}')


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
    if util.file_exists(path):
        second(path)
