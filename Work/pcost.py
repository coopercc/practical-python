# pcost.py
#
# Exercise 1.27

import csv
import sys


##
def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {i}: Couldn't convert {row}")

    return total_cost


cost = portfolio_cost("Data/portfoliodate.csv")
# cost = portfolio_cost("Data/missing.csv")
print(cost)
