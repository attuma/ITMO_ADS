import unittest
import time
import tracemalloc
import random
import sys
from lab3.task1 import randomized_quicksort

sys.setrecursionlimit(20000)


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
        copy = arr.copy()
        expected = sorted(arr)

        tracemalloc.start()
        start = time.perf_counter()

        randomized_quicksort(copy, 0, len(copy) - 1)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(copy, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_example(self):
        data = [2, 3, 9, 2, 2]
        self.run_test("Пример из задачи", data)

    def test_2_min(self):
        data = [random.randint(-100, 100)]
        self.run_test("Нижняя граница (N=1)", data)

    def test_3_sorted(self):
        data = list(range(1000))
        self.run_test("Отсортированный (Наилучший)", data)

    def test_4_reverse(self):
        data = list(range(1000, 0, -1))
        self.run_test("Обратный порядок (Наихудший)", data)

    def test_5_duplicates(self):
        data = [random.choice([1, 2, 3]) for _ in range(1000)]
        self.run_test("Много дубликатов", data)

    def test_6_max(self):
        data = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10000)]
        self.run_test("Верхняя граница (N=10^4)", data)


if __name__ == "__main__":
    unittest.main()