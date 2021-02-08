# pcost.py
#
# Exercise 1.27

total = 0
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
for line in f:
    row = line.split(',')
    line_total = float(row[1]) * float(row[2])
    total = total + line_total
f.close()
output = f'Total cost: ${total:0.2f}'
print(output)
