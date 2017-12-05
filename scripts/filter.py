from datetime import datetime

def filter(data, filter):
	count = 0
	filtered = []
#	filtered = data

	print("data length BEFORE being filtered", len(data))

	data[:] = [item for item in data if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour == filter and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 6]
#	for item in filtered:
#		if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour != filter or datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() == 5 or datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S') == 6:
#			del filtered[filtered.index(item)]
#			count += 1

#	for item in range(8760):
#		if datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S').hour == filter and datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(data[item]['date'], '%m-%d-%Y %H:%M:%S') != 6:
#			filtered.append(data[item])
#			count += 1


#	for item in data:
#		if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour == filter and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 6:
#			filtered.append(item)
#			count += 1

	print("data length AFTER being filtered: ", len(data))
	#print(filtered)

	return data

def filterfrom19to05(data):
	filtered = []
	for item in data:
		#print(item['date'])
		hour = datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour
		if hour == 19 or hour == 20 or hour == 21 or hour == 22 or hour == 23 or hour == 0 or hour == 1 or hour == 2 or hour == 3 or hour == 4 or hour == 5:
			filtered.append(item)
	#print(filtered)
	return filtered
