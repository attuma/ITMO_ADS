def bureaucracy(n, m, arr):
    sorted_arr = sorted(arr)
    subtracted = 0
    prev_val = 0

    for i, val in enumerate(sorted_arr):
        diff = val - prev_val
        if diff == 0:
            continue

        count = n - i
        cost = diff * count

        if m >= cost:
            m -= cost
            subtracted = val
            prev_val = val
        else:
            rounds = m // count
            rem = m % count
            subtracted += rounds
            m = rem
            break

    survivors = []
    for x in arr:
        if x > subtracted:
            survivors.append(x - subtracted)

    if not survivors:
        return [-1]

    res = []
    for i in range(m, len(survivors)):
        res.append(survivors[i])

    for i in range(m):
        val = survivors[i] - 1
        if val > 0:
            res.append(val)

    return res if res else [-1]