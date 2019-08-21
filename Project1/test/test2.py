from unittest import TestCase
from source.main import Calculator


class TestCaulculator2(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum2(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

