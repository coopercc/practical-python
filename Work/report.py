# report.py
#
# Exercise 2.4

import sys
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a portfolio file and return a list of dictionaries.
    """
    return parse_csv(
        filename, select=["name", "shares", "price"], types=[str, int, float]
    )


def read_prices(filename):
    pricelist = parse_csv(filename, types=[str, float], has_headers=False)
    return dict(pricelist)


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


def main(args):
    if len(args) != 3:
        raise SystemExit(f"Usage: {args[0]} " "portoliofile pricefile")
    portfolio_report(args[1], args[2])


# portfolio_report("Data/portfoliodate.csv", "Data/prices.csv")

if __name__ == "__main__":
    main(sys.argv)
