# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    'Read portfolio file into list of dictionaries'
    portfolio = []

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
    prices = dict()

    f = open(filename, 'r')
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

#from pprint import pprint

portfolio = read_portfolio('Data/portfoliodate.csv')
#pprint(portfolio)

prices = read_prices('Data/prices.csv')
#pprint(prices)

headers = ('Name', 'Shares', 'Price', 'Change')
separator = ''
header = ''

for name in headers:
    header += f'{name:>10s} '
    separator += (10 * '-') + ' '
print(f'{header}\n{separator}')

report = make_report(portfolio, prices)
for r in report:
    rep = '%10s %10d %10s %10.2f' % r
    print(rep)
