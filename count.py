import csv

data = open('iowa-liquor-sample.csv', 'r')

counter = 0

for line in data:
	if 'single malt scotch' in line.lower():
		counter += 1

print counter
