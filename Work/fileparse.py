# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str, select: list[str] = None, types=None, has_headers=True, delimiter=","
) -> list[dict[str, str]]:
    """
    parse a csv file into a list of records
    allows user to specify column names to keep
    """
    with open(filename, "rt") as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colName) for colName in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # skip empty ones
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records
