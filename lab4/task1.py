def stack_process(commands):
    stack = []
    removed = []

    for cmd in commands:
        if cmd.startswith('+'):
            _, num = cmd.split()
            stack.append(int(num))
        elif cmd == '-':
            removed.append(stack.pop())

    return removed

