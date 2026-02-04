with open('input.txt', 'r') as f:
    a, b = map(int, f.readline().split())

res1 = a + b
res2 = a + b**2

with open('output.txt', 'w') as f:
    f.write(str(res1) + "\n")
    f.write(str(res2))