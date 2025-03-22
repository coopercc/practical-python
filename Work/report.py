# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """
    Read a portfolio file and return a list of dictionaries.
    """
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


def print_report(report):
    """
    Print a report of the portfolio.
    """
    headers = ("Name", "Shares", "Price", "Change")

    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))

    for r in report:
        print("%10s %10d %10s %10.2f" % (r[0], r[1], f"${r[2]:.2f}", r[3]))


def portfolio_report(portfolio_filename, prices_filename):
    """
    Read a portfolio file and a prices file, and print a report.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report("Data/portfoliodate.csv", "Data/prices.csv")
