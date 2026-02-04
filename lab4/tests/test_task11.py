import unittest
import time
import tracemalloc
import random
from lab4.task11 import bureaucracy


class TestTask11(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, n, m, arr, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = bureaucracy(n, m, arr)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_example_1(self):
        self.run_test("Пример 1", 3, 2, [1, 2, 3], [3, 1])

    def test_2_example_2(self):
        self.run_test("Пример 2", 4, 5, [2, 5, 2, 3], [4, 1, 2])

    def test_3_empty(self):
        self.run_test("Все ушли", 3, 10, [1, 2, 3], [-1])

    def test_4_large(self):
        n = 100000
        m = 10 ** 8
        arr = [random.randint(1, 10 ** 6) for _ in range(n)]

        tracemalloc.start()
        start = time.perf_counter()
        bureaucracy(n, m, arr)
        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.results.append(["Верхняя граница (N=10^5)", f"{end - start:.6f} сек", f"{peak} байт"])


if __name__ == "__main__":
    unittest.main()