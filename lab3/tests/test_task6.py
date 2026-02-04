import unittest
import time
import tracemalloc
import random
from lab3.task6 import solve_sort


class TestTask6(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, a, b, expected=None):
        tracemalloc.start()
        _ = solve_sort(a, b)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        start = time.perf_counter()
        res = solve_sort(a, b)
        end = time.perf_counter()

        if expected is not None:
            self.assertEqual(res, expected)

        self.results.append([name, f"{end - start:.6f} сек", f"{peak / 1024 / 1024:.2f} Мб"])

    def test_1_min(self):
        self.run_test("Нижняя граница (1x1)", [2], [3], 6)

    def test_2_example(self):
        a = [7, 1, 4, 9]
        b = [2, 7, 8, 11]
        self.run_test("Пример из задачи", a, b, 51)

    def test_3_medium(self):
        a = [random.randint(0, 100) for _ in range(100)]
        b = [random.randint(0, 100) for _ in range(100)]
        self.run_test("Средний (100x100)", a, b)

    def test_4_upper_bound(self):
        a = [random.randint(0, 40000) for _ in range(2000)]
        b = [random.randint(0, 40000) for _ in range(2000)]
        self.run_test("Верхняя граница (2000x2000)", a, b)


if __name__ == "__main__":
    unittest.main()