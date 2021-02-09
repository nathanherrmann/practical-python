# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = [] 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = [{headers[0] : row[0]}, {headers[1] : int(row[1])}, {headers[2] : float(row[2])}]
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    try:
        f = open(filename, 'r')
        rows = csv.reader(f)
        for row in rows:
            print(row)

    except:
        print('There was an error')
