# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
  total = 0
  f = open(filename, 'rt')
  headers = next(f).split(',')
  for line in f:
      row = line.split(',')
      line_total = float(row[1]) * float(row[2])
      total = total + line_total
  f.close()
  return total
  
cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: ${cost:0.2f}')
