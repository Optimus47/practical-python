# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total = 0.0

    with open(filename,'rt') as f:
        rows = csv.reader(f)
        next(f) #headers
        for row in rows:
            #row = line.strip().split(',')
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", line)
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

