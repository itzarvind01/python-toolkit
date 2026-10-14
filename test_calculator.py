
import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, "+", 20), 30)

    def test_subtraction(self):
        self.assertEqual(calculate(20, "-", 5), 15)

    def test_multiplication(self):
        self.assertEqual(calculate(5, "*", 4), 20)

    def test_division(self):
        self.assertEqual(calculate(20, "/", 4), 5)

    def test_percentage_remainder(self):
        self.assertEqual(calculate(100, "%", 30), 10)

    def test_power(self):
        self.assertEqual(calculate(2, "**", 5), 32)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10, "/", 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(10, "&", 2)


if __name__ == "__main__":
    unittest.main()
