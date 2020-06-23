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

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
