def solve_sort(arr_a, arr_b):
    c = [x * y for x in arr_a for y in arr_b]
    c.sort()
    total = 0
    for i in range(0, len(c), 10):
        total += c[i]
    return total
