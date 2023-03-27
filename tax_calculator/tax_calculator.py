"""
Given a list of progressive tax brackets, write a solution to calculate the tax on a given income.

Let's start with the following tax brackets:
You are taxed 10% on the first $10,000, 20% on the next $20,000, 30% on the next $15,000 and 50% on any amount remaining

Example:
  Input: 100,000
  Output: 37,000

  As you know, taxes can change from year to year. Update your solution to store the different annual tax brackets and incomes to allow for historical comparisons.

  You are taxed 10% on the first $5,000, 20% on the next $30,000, and 50% on any amount remaining

tax_brackets_list = {
  "2001": [
    (10_000, .1),
    (30_000, .2),
    (45_000, .3)
  ],
  "2002": [
    (5_000, .1),
    (30_000, .2),
  ]
}
"""

tax_brackets = {
  "2001": [
    (10_000, .1),
    (20_000, .2),
    (15_000, .3),
    (0, .5)
  ],
  "2002": [
    (5_000, .1),
    (30_000, .2),
    (0, .5)
  ]
}


def calculate_taxes_from_bracket(income: float, tax_brackets: list):
    tax_responsiblity = 0
    rolling_income_total = 0

    if income == 0:
        return 0

    for i, tax_bracket in enumerate(tax_brackets):
        if i == len(tax_brackets) - 1:  # At the last tax bracket
            tax_responsiblity += (income - rolling_income_total) * tax_bracket[1]
        elif income < tax_bracket[0]:  # found out bracket
            taxable_income = income - rolling_income_total
            tax_responsiblity += taxable_income * tax_bracket[1]
            break
        else:
            rolling_income_total += tax_bracket[0]
            tax_responsiblity += tax_bracket[0] * tax_bracket[1]

    return tax_responsiblity


def calculate_taxes(income: float, tax_brackets: dict) -> dict:
    tax_responsibilities = {}

    for key in tax_brackets:
        tax_responsibilities[key] = calculate_taxes_from_bracket(income, tax_brackets[key])

    return tax_responsibilities


