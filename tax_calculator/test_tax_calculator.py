from tax_calculator import calculate, calculate_income_tax, main
from unittest import TestCase
from unittest.mock import patch


class TestCalculator(TestCase):
    def test_calculate(self):
        result = calculate(100000, 10)
        self.assertEqual(result, 10000)

    def test_calculate_income_tax(self):
        result = calculate_income_tax(500000)
        self.assertEqual(result, 12500.0)

    @patch("tax_calculator.get_input", return_value=500000)
    @patch("builtins.print")
    def test_main(self, mock_patch_print, mock_patch_input):
        main()
        # Careful here: This gets called a million times trying to print the output of the unit test.
        mock_patch_print.assert_called_with('Total tax applicable at $500000.0 is $12500.0')







