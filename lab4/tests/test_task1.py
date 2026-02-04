import unittest
import time
import tracemalloc
import random
from lab4.task1 import stack_process


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

    def run_test(self, name, commands, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = stack_process(commands)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_min(self):
        cmds = ["+ 5", "-"]
        self.run_test("Нижняя граница (2 команды)", cmds, [5])

    def test_2_example(self):
        cmds = ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-"]
        expected = [10, 1234]
        self.run_test("Пример из задачи", cmds, expected)

    def test_3_large(self):
        cmds = [f"+ {i}" for i in range(5000)] + ["-" for _ in range(5000)]
        expected = list(range(4999, -1, -1))
        self.run_test("Средняя нагрузка (10000 команд)", cmds, expected)

    def test_4_upper_bound(self):
        n = 500000
        cmds = [f"+ {i}" for i in range(n)] + ["-" for _ in range(n)]
        expected = list(range(n - 1, -1, -1))
        self.run_test("Верхняя граница (10^6 команд)", cmds, expected)


if __name__ == "__main__":
    unittest.main()