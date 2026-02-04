import sys
import random

sys.setrecursionlimit(20000)

def partition3(A, l, r):
    x = A[l]
    m1 = l
    m2 = r
    i = l + 1
    while i <= m2:
        if A[i] < x:
            A[i], A[m1] = A[m1], A[i]
            m1 += 1
            i += 1
        elif A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2

def randomized_quicksort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    m1, m2 = partition3(A, l, r)
    randomized_quicksort(A, l, m1 - 1)
    randomized_quicksort(A, m2 + 1, r)
