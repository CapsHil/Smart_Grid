from datetime import datetime

def filter(data, filter):
	count = 0
	filtered = []
	for item in range(8760):
		if datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S').hour == filter and datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S') != 6:
			filtered.append(data[item])
			count += 1
#	for item in data:
#		if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour == filter and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 6:
#			filtered.append(item)
#			count += 1
	print(count)
	return filtered
