import json
import csv
from datetime import date, datetime, timedelta

januaryFirst = datetime(2015, 1, 1, 0, 0, 0)
newYearsEve = datetime(2016, 1, 1, 0, 0, 0)

out = []
parsedData = []

def perdelta(start, end, delta):
	curr = start
	while curr < end:
		yield curr
		curr += delta

def parse():
	for result in perdelta(januaryFirst, newYearsEve, timedelta(hours=1)):
		out.append(result.strftime('%m-%d-%Y %H:%M:%S'))



	with open('../ressources/Prix-spot-2015.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		i = 0
		for row in reader:
			temp = {'spot': row[0], 'date':out[i]}
			parsedData.append(temp)
			i = i+1

	print(json.dumps(parsedData))

	#returns spot price data with associated timestamp
	return json.dumps(parsedData)

parse()
