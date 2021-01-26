# bounce.py
#
# Exercise 1.5
height = 100
count = 1

while count <= 10:
	height = round(height * 3 / 5, 4)
	print(count, ' ', height)
	count = count + 1
