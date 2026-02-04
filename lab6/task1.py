def process_set(ops):
    m = 1000
    p = 1000000007
    a = 263
    b = 31

    table = [[] for _ in range(m)]
    res = []

    def get_hash(val):
        return ((a * val + b) % p) % m

    for op in ops:
        cmd, val_str = op.split()
        val = int(val_str)
        idx = get_hash(val)
        chain = table[idx]

        if cmd == 'A':
            found = False
            for x in chain:
                if x == val:
                    found = True
                    break
            if not found:
                chain.append(val)

        elif cmd == 'D':
            if val in chain:
                chain.remove(val)

        elif cmd == '?':
            found = False
            for x in chain:
                if x == val:
                    found = True
                    break
            res.append('Y' if found else 'N')

    return res
