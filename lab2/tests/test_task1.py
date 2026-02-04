import unittest
import time
import tracemalloc
import random
import sys
from lab2.task1 import merge_sort

sys.setrecursionlimit(200000)

class TestTask1(unittest.TestCase):
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
        start = time.perf_counter()

        if arr_copy:
            merge_sort(arr_copy, 0, len(arr_copy) - 1)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(arr_copy, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_simple(self):
        data = [12, 11, 13, 5, 6, 7]
        self.run_test("Пример из задачи", data)

    def test_2_reverse(self):
        data = list(range(1000, 0, -1))
        self.run_test("Обратная сортировка n = 1000", data)

    def test_3_sorted(self):
        data = list(range(1000))
        self.run_test("Уже отсортирован n = 1000", data)

    def test_4_random(self):
        data = [random.randint(-10**9, 10**9) for _ in range(1000)]
        self.run_test("Случайный массив n = 1000", data)

    def test_5_max(self):
        data = [random.randint(-1000, 1000) for _ in range(20000)]
        self.run_test("Верхняя граница", data)


if __name__ == "__main__":
    unittest.main()