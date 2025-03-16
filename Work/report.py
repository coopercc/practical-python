# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

print(portfolio)
print(prices)

current_value = 0.0
portfolio_gain = 0.0

for s in portfolio:
    current_price = prices[s["name"]]
    current_value += s["shares"] * current_price
    portfolio_gain += s["shares"] * (current_price - s["price"])

print(current_value)
print(portfolio_gain)
