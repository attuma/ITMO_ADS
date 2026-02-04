def check_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(text, 1):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack or stack[-1][0] != pairs[char]:
                return str(i)
            stack.pop()

    if not stack:
        return "Success"
    else:
        return str(stack[0][1])
