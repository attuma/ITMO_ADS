import unittest
import time
import tracemalloc
import random
from lab5.task7 import heap_sort

class TestTask7(unittest.TestCase):
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

        res = heap_sort(copy)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_lower_bound(self):
        data = [random.randint(-100, 100)]
        self.run_test("Нижняя граница (N=1)", data)

    def test_2_random(self):
        data = [random.randint(-100, 100) for _ in range(1000)]
        self.run_test("Случайный массив (N=1000)", data)

    def test_3_reverse(self):
        data = list(range(1000, 0, -1))
        self.run_test("Обратный порядок (N=1000)", data)

    def test_4_upper_bound(self):
        # N=10^5
        data = [random.randint(-10**9, 10**9) for _ in range(100000)]
        self.run_test("Верхняя граница (N=10^5)", data)

if __name__ == "__main__":
    unittest.main()