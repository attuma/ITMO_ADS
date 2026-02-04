import unittest
import time
import tracemalloc
import random
from lab3.task3 import scarecrow_sort


class TestTask3(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, n, k, arr, expected):
        copy = arr.copy()

        tracemalloc.start()
        start = time.perf_counter()

        res = scarecrow_sort(n, k, copy)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_min(self):
        data = [10]
        self.run_test("Нижняя граница (N=1)", 1, 1, data, "ДА")

    def test_2_example_true(self):
        data = [1, 5, 3, 4, 1]
        self.run_test("Пример (ДА)", 5, 3, data, "ДА")

    def test_3_example_false(self):
        data = [2, 1, 3]
        self.run_test("Пример (НЕТ)", 3, 2, data, "НЕТ")

    def test_4_max(self):
        data = sorted([random.randint(-10**9, 10**9) for _ in range(100000)])
        self.run_test("Верхняя граница (N=100000)", 100000, 5, data, "ДА")


if __name__ == "__main__":
    unittest.main()