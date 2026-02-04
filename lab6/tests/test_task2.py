import unittest
import time
import tracemalloc
from lab6.task2 import phone_book


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

    def run_test(self, name, cmds, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = phone_book(cmds)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)

        memory_mb = peak / 1024 / 1024
        self.results.append([name, f"{end - start:.6f} сек", f"{memory_mb:.2f} Мб"])

    def test_1_lower_bound(self):
        cmds = ["add 12345 me", "find 12345"]
        expected = ["me"]
        self.run_test("Нижняя граница (N=2)", cmds, expected)

    def test_2_example_1(self):
        cmds = [
            "add 911 police", "add 76213 Mom", "add 17239 Bob",
            "find 76213", "find 910", "find 911", "del 910", "del 911",
            "find 911", "find 76213", "add 76213 daddy", "find 76213"
        ]
        expected = ["Mom", "not found", "police", "not found", "Mom", "daddy"]
        self.run_test("Пример 1 (Базовый)", cmds, expected)

    def test_3_example_2(self):
        cmds = [
            "find 3839442", "add 123456 me", "add 0 granny",
            "find 0", "find 123456", "del 0", "del 0", "find 0"
        ]
        expected = ["not found", "granny", "me", "not found"]
        self.run_test("Пример 2 (Граничные случаи)", cmds, expected)

    def test_4_upper_bound(self):
        n = 100000
        cmds = [f"add {i} User{i}" for i in range(n // 2)] + [f"find {i}" for i in range(n // 2)]
        expected = [f"User{i}" for i in range(n // 2)]
        self.run_test("Верхняя граница (N=10^5)", cmds, expected)


if __name__ == "__main__":
    unittest.main()