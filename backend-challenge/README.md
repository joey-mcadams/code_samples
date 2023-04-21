# Cube Python Code Challenge

In this repository, there's a directory called `project`. It contains a standalone Django application. The
application has one app called `dimensions`. In addition, there's a SQLite database with tables and rows
already prepopulated.

## Get Started

1. Clone this repository `git clone https://github.com/cube-planning/backend-challenge.git`
2. `cd backend-challenge/`
3. Start a virtual environment (if desired)
4. `cd project/`
5. Install requirements `pip install -r requirements.txt`
6. Try `python manage.py check_answers` to see there are failing tests!

Read on to find out how to make the tests pass...

## Models

You are given the _ `Company` and `Dimension` in `dimensions/models.py`.  A `Company` has a hierarchy of
`Dimension` objects as defined by this schema.

A `parent` value of `None` means that `Dimension` instance is a top-level `Dimension` with no
parents of its own. The hierarchy can be nested up to 10 levels deep.

## Challenges

You'll find the code for the challenge assignments in `dimensions/challenge.py`. Below is an explanation of what we're looking for.
Note: Recursion within the Python side is allowed, but **do not** use a `RECURSIVE` SQL query statement for either of these assignments.

### Assignment 1: `list_children(dimension_id)`

Given a dimension ID, write a function that iterates through all its children and returns a list of strings
representing the nested hierarchy of its children.

#### Example:

```python
>>> from dimensions.challenge import list_children
>>> balance_sheet_id = 8
>>> [print(row) for row in list_children(balance_sheet_id)]
Balance Sheet
	Assets
	Equity
	Liabilities

>>> list_children(balance_sheet_id)
[
    'Balance Sheet',
    '\tAssets',
    '\tEquity',
    '\tLiabilities',
]
```

### Assignment 2: `list_hierarchy(company_id)`

Given a company ID, write a function that iterates through all of that company's dimensions and returns a list
of strings representing the nested hierarchy.

Bonus points: Also include a version of this that only makes one query against the database. For this bonus solution do not use a `RECURSIVE` SQL query.

#### Example:

```python
>>> from dimensions.challenge import list_hierarchy
>>> company_id = 1
>>> [print(row) for row in list_hierarchy(company_id)]
Account
	Balance Sheet
		Assets
		Equity
		Liabilities
	Income Statement
		Expense
		Net Income
		Revenue
			Product Revenue
			Services Revenue
Department
	All Departments
		General & Administrative
			Finance & Accounting
			Human Resources
			Operations
		Marketing
		Product
			Design
			Engineering
Scenario
	Actuals
	Budget

>>> list_hierarchy(company_id)
[
    'Account',
    '\tBalance Sheet',
    '\t\tAssets',
    '\t\tEquity',
    '\t\tLiabilities',
    '\tIncome Statement',
    '\t\tExpense',
    '\t\tNet Income',
    '\t\tRevenue',
    '\t\t\tProduct Revenue',
    '\t\t\tServices Revenue',
    'Department',
    '\tAll Departments',
    '\t\tGeneral & Administrative',
    '\t\t\tFinance & Accounting',
    '\t\t\tHuman Resources',
    '\t\t\tOperations',
    '\t\tMarketing',
    '\t\tProduct',
    '\t\t\tDesign',
    '\t\t\tEngineering',
    'Scenario',
    '\tActuals',
    '\tBudget'
]
```

### Check Your Answers

You can check your answers using `python manage.py check_answers`

### Hint

`db.sqlite3` has data in it! You can use the Django shell to explore the models and run your code.

## Submit Your Answers

When you're done, zip up your response and email it back to the Cube Recruiting team member you are working with!

### Extra Questions

When you push up your copy of the repo, answer these questions in your copy of README.md

1. Explain what SQL queries your solution is making and why.
2. Assume there are hundreds of dimensions and the hierarchy is loaded on every page load. What caching strategies
would you suggest?
    - Hint: The answer here is not a SQL query using `RECURSIVE`.
