import time
import tracemalloc
from task2 import get_fib
from task3 import get_fib_last_digit

values = [10, 100, 1000, 5000, 10000, 20000]

print(f"{'N':<10} | {'T2 Время':<12} | {'T2 Память':<12} | {'T3 Время':<12} | {'T3 Память':<12}")
print("-" * 70)

for n in values:
    tracemalloc.start()
    t0 = time.perf_counter()
    get_fib(n)
    t1 = time.perf_counter()
    _, peak2 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time2 = t1 - t0

    tracemalloc.start()
    t0 = time.perf_counter()
    get_fib_last_digit(n)
    t1 = time.perf_counter()
    _, peak3 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time3 = t1 - t0

    print(f"{n:<10} | {time2:.6f} сек | {peak2:<10} байт | {time3:.6f} сек | {peak3:<10} байт")