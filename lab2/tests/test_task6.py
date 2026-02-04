import unittest
import time
import tracemalloc
import random
from lab2.task6 import find_max


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

    def solve_naive(self, arr):
        if not arr: return 0
        m_sum = float('-inf')
        for i in range(len(arr)):
            curr = 0
            for j in range(i, len(arr)):
                curr += arr[j]
                m_sum = max(m_sum, curr)
        return m_sum

    def run_test(self, name, arr):
        tracemalloc.start()
        start = time.perf_counter()

        if not arr:
            res_sum = 0
        else:
            _, _, res_sum = find_max(arr, 0, len(arr) - 1)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if len(arr) <= 1000:
            expected = self.solve_naive(arr)
            self.assertEqual(res_sum, expected)

        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_lower_bound(self):
        data = [100]
        self.run_test("Нижняя граница ", data)

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