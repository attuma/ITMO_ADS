import unittest
import time
import tracemalloc
from lab6.task7 import solve_stones


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

    def run_test(self, name, n, k, s, pairs, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = solve_stones(n, k, s, pairs)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_lower_bound(self):
        self.run_test("Нижняя граница (N=1)", 1, 1, "a", ["ab"], 0)

    def test_2_example_1(self):
        self.run_test("Пример 1", 7, 1, "abacaba", ["aa"], 6)

    def test_3_example_2(self):
        pairs = ["ab", "ac", "bb"]
        self.run_test("Пример 2", 7, 3, "abacaba", pairs, 7)

    def test_4_upper_bound(self):
        n = 10000
        s = "a" * n
        pairs = ["aa"]
        expected = n * (n - 1) // 2
        self.run_test("Верхняя граница (N=10000)", n, 1, s, pairs, expected)


if __name__ == "__main__":
    unittest.main()