# report.py
#
# Exercise 2.4

import sys
import tableformat
from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    """
    Read a portfolio file and return a list of dictionaries.
    """
    with open(filename) as lines:
        portfolio_dicts = parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )

        portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portfolio_dicts]

        return portfolio


def read_prices(filename):
    with open(filename) as lines:
        pricelist = parse_csv(lines, types=[str, float], has_headers=False)
        return dict(pricelist)


def make_report(portfolio: list[Stock], prices):
    report = []
    for s in portfolio:
        line = (
            s.name,
            s.shares,
            prices[s.name],
            prices[s.name] - s.price,
        )
        report.append(line)

    return report


def print_report(report, formatter: tableformat.TableFormatter):
    """
    Print a report of the portfolio.
    """
    # headers = ("Name", "Shares", "Price", "Change")

    formatter.headings(["Name", "Shares", "Price", "Change"])
    # print("%10s %10s %10s %10s" % headers)
    # print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price: 0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

    # for r in report:
    #     print("%10s %10d %10s %10.2f" % (r[0], r[1], f"${r[2]:.2f}", r[3]))


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    """
    Read a portfolio file and a prices file, and print a report.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f"Usage: {args[0]} " "portoliofile pricefile format")
    portfolio_report(args[1], args[2], args[3])


# portfolio_report("Data/portfoliodate.csv", "Data/prices.csv")

if __name__ == "__main__":
    main(sys.argv)
