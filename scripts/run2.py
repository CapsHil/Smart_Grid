import parseCosts
import filter
from datetime import datetime

def run():
	costsSum = 0
	filtered = filter.filterfrom19to05(parseCosts.parse())
	for item in filtered:
                hour = datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour
		if hour == 21:
		        costsSum += float(item['spot'])*0.0704
		if hour == 22:
			costsSum += float(item['spot'])*0.169
		if hour == 23:
			costsSum += float(item['spot'])*0.2394
		if hour == 00:
			costsSum += float(item['spot'])*0.2113
		if hour == 01:
			costsSum += float(item['spot'])*0.1408
		if hour == 02:
			costsSum += float(item['spot'])*0.0845
		if hour == 03:
			costsSum += float(item['spot'])*0.0563
		if hour == 04:
			costsSum += float(item['spot'])*0.0282
	print(costsSum*6)
run()
