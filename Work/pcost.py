# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    portfolio = read_portfolio(filename)
    for item in portfolio:
        total_cost += item.shares * item.price

    return total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit(f"Usage: {args[0]} " "portoliofile pricefile")
    print(portfolio_cost(args[1]))


if __name__ == "__main__":
    main(sys.argv)
