# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str,
    select: list[str] = None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
) -> list[dict[str, str]]:
    """
    parse a csv file into a list of records
    allows user to specify column names to keep
    """

    # we add this check specifically because it prevents running non-sensical code.
    if select and not has_headers:
        raise RuntimeError("select argument requires headers")

    with open(filename, "rt") as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colName) for colName in select]
            headers = select
        else:
            indices = []

        records = []
        for index, row in enumerate(rows):
            try:
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
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {index}: couldn't convert {row}")
                    print(f"Row {index}: reason {e}")
            records.append(record)

        return records
