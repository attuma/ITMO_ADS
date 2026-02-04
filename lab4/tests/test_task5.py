import unittest
import time
import tracemalloc
import random
from lab4.task5 import max_stack


class TestTask5(unittest.TestCase):
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

        res = max_stack(commands)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_example(self):
        cmds = ["push 2", "push 1", "max", "pop", "max"]
        self.run_test("Пример из задачи 1", cmds, [2, 2])

    def test_2_example_mix(self):
        cmds = ["push 1", "push 2", "max", "pop", "max"]
        self.run_test("Пример из задачи 2", cmds, [2, 1])

    def test_3_increasing(self):
        cmds = [f"push {i}" for i in range(1000)] + ["max"]
        self.run_test("Растущая последовательность", cmds, [999])

    def test_4_upper_bound(self):
        n = 130000
        cmds = []
        for i in range(n):
            cmds.append(f"push {i}")
        cmds.append("max")
        for i in range(n):
            cmds.append("pop")

        self.run_test("Верхняя граница (N=400000)", cmds, [n - 1])


if __name__ == "__main__":
    unittest.main()