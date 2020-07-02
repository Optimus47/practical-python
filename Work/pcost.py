# pcost.py
#
# Exercise 1.27
import csv
import sys

import report

def portfolio_cost(filename):
    total = 0.0
    for row in report.read_portfolio(filename):
        total += row['shares'] * row['price']
    return total


    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total

def main(argv=None):
    if argv and len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
