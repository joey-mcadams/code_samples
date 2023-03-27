from .tax_calculator import calculate_taxes, tax_brackets
from unittest import TestCase


class TestCalculator(TestCase):
    def test_calculate(self):
        taxes = calculate_taxes(0, tax_brackets)
        self.assertEqual({'2001': 0, '2002': 0}, taxes)

        taxes = calculate_taxes(17000, tax_brackets)
        self.assertEqual({'2001': 2400.0, '2002': 2900.0}, taxes)

        taxes = calculate_taxes(100000, tax_brackets)
        self.assertEqual({'2001': 37000.0, '2002': 39000.0}, taxes)

    # assert calculate_taxes(0, tax_brackets) == 0
    # assert calculate_taxes(17_000, tax_brackets) == 2_400
    # assert calculate_taxes(100_000, tax_brackets) == 37_000






