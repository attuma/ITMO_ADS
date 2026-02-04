def get_fib(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.read())

    res = get_fib(n)

    with open('output.txt', 'w') as f:
        f.write(str(res))