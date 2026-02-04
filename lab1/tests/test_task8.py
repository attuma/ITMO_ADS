import unittest
import time
import tracemalloc
import random
from lab1.task8 import *


class TestSwapSort(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, arr):
        arr_copy = arr.copy()
        expected = sorted(arr)

        tracemalloc.start()
        start_time = time.perf_counter()

        swap_sort(arr_copy)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(arr_copy, expected)

        self.results.append([name, f"{end_time - start_time:.6f} сек", f"{peak} байт"])

    def test_1_lower_bound(self):
        data = [random.randint(1, 100) for _ in range(3)]
        self.run_test("Нижняя граница (N=3)", data)

    def test_2_example(self):
        data = [3, 1, 4, 2, 2]
        self.run_test("Пример из задачи 1", data)

    def test_3_example(self):
        data = [10, 20, 5, 15, 30]
        self.run_test("Пример из задачи 2", data)

    def test_4_upper_bound(self):
        data = [random.randint(-10 ** 9, 10 ** 9) for _ in range(5000)]
        self.run_test("Верхняя граница (N=5000)", data)


if __name__ == "__main__":
    unittest.main()