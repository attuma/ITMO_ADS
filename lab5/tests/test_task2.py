import unittest
import time
import tracemalloc
from lab5.task2 import tree_height


class TestTask2(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, n, parents, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = tree_height(n, parents)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_lower_bound(self):
        self.run_test("Нижняя граница (N=1)", 1, [-1], 1)

    def test_2_example_1(self):
        parents = [4, -1, 4, 1, 1]
        self.run_test("Пример 1 из задачи", 5, parents, 3)

    def test_3_example_2(self):
        parents = [-1, 0, 4, 0, 3]
        self.run_test("Пример 2 из задачи", 5, parents, 4)

    def test_4_upper_bound(self):
        n = 100000
        parents = [-1] + [i for i in range(n - 1)]
        self.run_test("Верхняя граница (N=10^5, Линия)", n, parents, n)


if __name__ == "__main__":
    unittest.main()