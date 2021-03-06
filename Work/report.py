# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    'Read portfolio file into list of dictionaries'
    portfolio = []
    return parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
    'Read prices into dict'
    prices = {}
    return  dict(parse_csv(filename,has_headers=False))

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        try:
            for name,price in rows:
               prices[name] = price
        except ValueError:
            pass
    return prices

def make_report(portfolio, prices):
    'Count changes in report'
    report = list()

    for line in portfolio:
        report.append((line['name'], line['shares'], '$'+str(line['price']), float(prices[line['name']])-float(line['price'])))

    return report

def print_report(headers, report):
    'Print report in a table'
    header, separator = '', ''
    for name in headers:
        header += f'{name:>10s} '
        separator += (10 * '-') + ' '
    print(f'{header}\n{separator}')

    for row in report:
        print('%10s %10d %10s %10.2f' % row)

def portfolio_report(file_portfolio, file_prices):
    'Top level function'
    portfolio = read_portfolio(file_portfolio)
    prices = read_prices(file_prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    report = make_report(portfolio, prices)
    print_report(headers, report)

def main(argv=['report.py', 'Data/portfolio.csv', 'Data/prices.csv']):
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
