import unittest
import time
import tracemalloc
from lab6.task1 import process_set  # Убедись, что твоя новая функция называется process_set


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

    def run_test(self, name, ops, expected):
        tracemalloc.start()
        process_set(ops)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        start = time.perf_counter()
        res = process_set(ops)
        end = time.perf_counter()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak / 1024 / 1024:.2f} Мб"])

    def test_1_lower_bound(self):
        ops = ["A 10", "? 10", "? 5"]
        expected = ["Y", "N"]
        self.run_test("Нижняя граница (N=3)", ops, expected)

    def test_2_example(self):
        ops = [
            "A 2", "A 5", "A 3", "? 2", "? 4", "A 2", "D 2", "? 2"
        ]
        expected = ["Y", "N", "N"]
        self.run_test("Пример из задачи", ops, expected)

    def test_3_upper_bound(self):
        n = 100000
        add_ops = [f"A {i}" for i in range(n)]
        check_ops = [f"? {i}" for i in range(n)]
        ops = add_ops + check_ops

        expected = ["Y"] * n
        self.run_test("Верхняя граница (N=10^5)", ops, expected)


if __name__ == "__main__":
    unittest.main()