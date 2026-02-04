import unittest
import time
import tracemalloc
import random
from lab4.task4 import check_brackets


class TestTask4(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        print("\n" + "=" * 80)
        print(f"{'Тест':<40} | {'Время выполнения':<20} | {'Затраты памяти':<15}")
        print("-" * 80)
        for row in cls.results:
            print(f"{row[0]:<40} | {row[1]:<20} | {row[2]:<15}")
        print("=" * 80 + "\n")

    def run_test(self, name, text, expected):
        tracemalloc.start()
        start = time.perf_counter()

        res = check_brackets(text)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res, expected)
        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_example_success(self):
        self.run_test("Пример 1 (Success)", "[]", "Success")

    def test_2_example_fail(self):
        self.run_test("Пример 2 (Ошибка закрывающей)", "{[}", "3")

    def test_3_example_fail_open(self):
        self.run_test("Пример 3 (Лишняя открывающая)", "{", "1")

    def test_4_upper_bound(self):
        data = "(" * 50000 + ")" * 50000
        self.run_test("Верхняя граница (N=100000)", data, "Success")


if __name__ == "__main__":
    unittest.main()