import unittest
import time
import tracemalloc
import random
import sys
from lab2.task6 import find_max
from lab2.task7 import find_max_linear

sys.setrecursionlimit(20000)


class TestTask7Comparison(unittest.TestCase):
    results = []

    @classmethod
    def tearDownClass(cls):
        header_fmt = "{:<25} | {:<12} | {:<12} | {:<10} | {:<10}"
        row_fmt = "{:<25} | {:<12} | {:<12} | {:<10} | {:<10}"

        print("\n" + "=" * 95)
        print(header_fmt.format("Тест", "Время (task6)", "Время (task7)", "Память (task6)", "Память (task7)"))
        print("-" * 95)

        for row in cls.results:
            print(row_fmt.format(row[0], row[1], row[2], row[3], row[4]))
        print("=" * 95 + "\n")

    def run_test(self, name, arr):
        tracemalloc.start()
        start_rec = time.perf_counter()

        if not arr:
            res_rec_sum = 0
        else:
            _, _, res_rec_sum = find_max(arr, 0, len(arr) - 1)

        end_rec = time.perf_counter()
        _, peak_rec = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tracemalloc.start()
        start_lin = time.perf_counter()

        if not arr:
            res_lin_sum = 0
        else:
            _, _, res_lin_sum = find_max_linear(arr)

        end_lin = time.perf_counter()
        _, peak_lin = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(res_rec_sum, res_lin_sum, f"Результаты алгоритмов не совпали в тесте {name}")

        time_rec_str = f"{end_rec - start_rec:.6f} с"
        time_lin_str = f"{end_lin - start_lin:.6f} с"
        mem_rec_str = f"{peak_rec} Б"
        mem_lin_str = f"{peak_lin} Б"

        self.results.append([name, time_rec_str, time_lin_str, mem_rec_str, mem_lin_str])

    def test_1_lower_bound(self):
        data = [100]
        self.run_test("Нижняя граница", data)

    def test_2_google_stocks(self):
        prices = [140]
        for _ in range(99):
            prices.append(prices[-1] + random.uniform(-5, 5))

        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        self.run_test("Акции Google n = 100", changes)

    def test_3_upper_bound(self):
        data = [random.randint(-1000, 1000) for _ in range(10000)]
        self.run_test("Верхняя граница", data)


if __name__ == "__main__":
    unittest.main()