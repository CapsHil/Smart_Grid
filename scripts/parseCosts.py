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
			temp = {'spot': row[0].replace(',', '.'), 'date':out[i]}
			if not (out[i].startswith("01-01") or out[i].startswith("04-06") or out[i].startswith("05-01") or out[i].startswith("05-08") or out[i].startswith("05-14") or out[i].startswith("05-25") or out[i].startswith("07-14") or out[i].startswith("08-15") or out[i].startswith("11-01") or out[i].startswith("11-11") or out[i].startswith("12-25")):
				parsedData.append(temp)
			i = i+1
		print(i)

	#print(parsedData)

	#returns spot price data with associated timestamp
	return parsedData

parse()
