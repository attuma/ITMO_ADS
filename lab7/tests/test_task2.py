import unittest
import time
import tracemalloc
from lab7.task2 import primitive_calculator


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

    def run_test(self, name, n, expected_len):
        tracemalloc.start()
        start = time.perf_counter()

        count, seq = primitive_calculator(n)

        end = time.perf_counter()
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertEqual(count, expected_len)
        self.assertEqual(seq[0], 1)
        self.assertEqual(seq[-1], n)

        for i in range(len(seq) - 1):
            valid = (seq[i + 1] == seq[i] + 1) or \
                    (seq[i + 1] == seq[i] * 2) or \
                    (seq[i + 1] == seq[i] * 3)
            self.assertTrue(valid)

        self.results.append([name, f"{end - start:.6f} сек", f"{peak} байт"])

    def test_1_min(self):
        self.run_test("Нижняя граница (N=1)", 1, 0)

    def test_2_example_1(self):
        self.run_test("Пример 1 (N=5)", 5, 3)

    def test_3_example_2(self):
        self.run_test("Пример 2 (N=96234)", 96234, 14)

    def test_4_max(self):
        self.run_test("Верхняя граница (N=10^6)", 1000000, 19)


if __name__ == "__main__":
    unittest.main()