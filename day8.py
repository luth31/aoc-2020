import util


def run_with_patch(memory: list, patch_idx: int) -> bool:
    memory = memory.copy()
    (opcode, value) = memory[patch_idx]

    if opcode == 'jmp':
        opcode = 'nop'
    elif opcode == 'nop':
        opcode = 'jmp'
    else:
        print(f'Not patching {memory[patch_idx]}.')
    memory[patch_idx] = (opcode, value)
    executed = []
    acc = 0
    ip = 0
    while ip < len(memory):
        if ip in executed:
            print(f'Boot looped at {ip}!')
            return False
        executed.append(ip)
        (opcode, value) = memory[ip]
        print(f'Exec {ip}')
        if opcode == 'nop':
            ip += 1
        elif opcode == 'acc':
            acc += value
            ip += 1
        elif opcode == 'jmp':
            ip += value
        if ip >= len(memory):
            print(f'The answer is {acc}')
            return True


def first(input_path: str) -> None:
    memory = []
    executed = []
    acc = 0
    ip = 0
    with open(input_path) as file:
        lines = file.read().split('\n')
    for line in lines:
        data = line.split(' ')
        memory.append((data[0], int(data[1])))
    while ip < len(memory):
        if ip in executed:
            print(f'The answer is {acc}')
            return
        executed.append(ip)
        (opcode, value) = memory[ip]
        if opcode == 'nop':
            ip += 1
        elif opcode == 'acc':
            acc += value
            ip += 1
        elif opcode == 'jmp':
            ip += value


def second(input_path: str) -> None:
    memory = []
    executed = []
    acc = 0
    ip = 0
    with open(input_path) as file:
        lines = file.read().split('\n')
    for line in lines:
        data = line.split(' ')
        memory.append((data[0], int(data[1])))
    # Run once to gather execution order
    while ip < len(memory):
        if ip in executed:
            break
        executed.append(ip)
        (opcode, value) = memory[ip]
        if opcode == 'nop':
            ip += 1
        elif opcode == 'acc':
            acc += value
            ip += 1
        elif opcode == 'jmp':
            ip += value
    # Try to patch starting at the end of the execution order list
    for i in reversed(executed):
        if run_with_patch(memory, i) is True:
            return


if __name__ == '__main__':
    path = util.get_input_path(__file__)
    if util.file_exists(path):
        first(path)
        second(path)
