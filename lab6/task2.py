def phone_book(ops):
    MAX_SIZE = 10000000
    book = [None] * MAX_SIZE
    res = []

    for op in ops:
        parts = op.split()
        cmd = parts[0]
        number = int(parts[1])

        if cmd == 'add':
            book[number] = parts[2]

        elif cmd == 'del':
            book[number] = None

        elif cmd == 'find':
            name = book[number]
            res.append(name if name is not None else "not found")

    return res