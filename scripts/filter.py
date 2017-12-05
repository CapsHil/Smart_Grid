from datetime import datetime

def filter(data, filter):
	filtered = []
	for item in data:
		#print(item['date'])
		if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour == 19:
			filtered.append(item)
	print(filtered)
	return filtered
