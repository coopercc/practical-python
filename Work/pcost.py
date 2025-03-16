# pcost.py
#
# Exercise 1.27

import csv
import sys


# def portfolio_cost(filename):
#     total_cost = 0

#     with open(filename, "rt") as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             try:

#                 total_cost = total_cost + (int(row[1]) * float(row[2]))
#             except ValueError:
#                 print("couldn't parse", row)

#     return total_cost


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost


# cost = portfolio_cost("Data/portfolio.csv")
# # cost = portfolio_cost("Data/missing.csv")


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = portfolio_cost(filename)
print("Total cost", cost)
