def max_stack(commands):
    stack = []
    results = []

    for cmd in commands:
        parts = cmd.split()
        op = parts[0]

        if op == "push":
            val = int(parts[1])
            curr_max = val
            if stack:
                curr_max = max(val, stack[-1][1])
            stack.append((val, curr_max))
        elif op == "pop":
            stack.pop()
        elif op == "max":
            results.append(stack[-1][1])

    return results