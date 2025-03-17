# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(headers, row))

            try:
                holding = {
                    "name": record["name"],
                    "shares": int(record["shares"]),
                    "price": float(record["price"]),
                }
            except ValueError:
                print(f"Row {i}: Couldn't convert {row}")
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


def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        line = (
            s["name"],
            s["shares"],
            prices[s["name"]],
            prices[s["name"]] - s["price"],
        )
        report.append(line)

    return report


portfolio = read_portfolio("Data/portfoliodate.csv")
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

report = make_report(portfolio, prices)
headers = ("Name", "Shares", "Price", "Change")

print("%10s %10s %10s %10s" % headers)
print(("-" * 10 + " ") * len(headers))

for r in report:
    print("%10s %10d %10s %10.2f" % (r[0], r[1], f"${r[2]:.2f}", r[3]))
