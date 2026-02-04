import unittest
import time
import tracemalloc
import random
from lab7.task4 import longest_common_subsequence


class TestTask4(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, a, b, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = longest_common_subsequence(a, b)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_example_1(self):
        a = [2, 7, 5]
        b = [2, 5]
        self.run_test("Пример 1", a, b, 2)

    def test_2_example_2(self):
        a = [7]
        b = [1, 2, 3, 4]
        self.run_test("Пример 2", a, b, 0)

    def test_3_example_3(self):
        a = [2, 7, 8, 3]
        b = [5, 2, 8, 7]
        self.run_test("Пример 3", a, b, 2)

    def test_4_max(self):
        n = 100
        a = [random.randint(1, 100) for _ in range(n)]
        b = [random.randint(1, 100) for _ in range(n)]
        tracemalloc.start()
        start = time.perf_counter()
        longest_common_subsequence(a, b)
        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.results.append(["Верхняя граница (N=100)", f"{end - start:.6f} сек", f"{peak} байт"])


if __name__ == "__main__":
    unittest.main()