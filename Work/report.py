# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
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

    for name, count, price in portfolio:
        report.append((name, count, '$'+str(price), float(prices[name])-float(price)))

    return report

from pprint import pprint

portfolio = read_portfolio('Data/portfolio.csv')
#pprint(portfolio)

prices = read_prices('Data/prices.csv')
#pprint(prices)

headers = ('Name', 'Shares', 'Price', 'Change')
separator = ''
header = ''

for name in headers:
    header += f'{name:>10s} '
    #print(f'{name:>10s}', end=' ')
    separator += (10 * '-') + ' '
print(f'{header}\n{separator}')

report = make_report(portfolio, prices)
for r in report:
    #print('%10s %10d %10.2f %10.2f' % r)
    rep = '%10s %10d %10s %10.2f' % r
    print(rep)
