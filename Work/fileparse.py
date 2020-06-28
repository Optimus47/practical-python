# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename,select=None,types=None,has_headers=True,delimiter=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)

        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for row in rows:
            if not row:
                continue
            if has_headers:
                if indices:
                    row = [ row[index] for index in indices ]
                if types:
                    row = [ func(val) for func, val in zip(types, row) ]
                record = dict(zip(headers, row))
            else:
                if types:
                    row = (func(val) for func, val in zip(types, row))
                record = tuple(row)
            records.append(record)

    return records
