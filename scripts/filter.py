from datetime import datetime

def filterWeekends(data):
    data[:] = [item for item in data if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 5 and datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').weekday() != 6]
    return data

def filter(data, filter):
	count = 0
	filtered = []

	print("data length BEFORE being filtered", len(data))
	data = filterWeekends(data)
	data[:] = [item for item in data if datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour == filter]
	print("data length AFTER being filtered: ", len(data))
	#print(filtered)

	return data

def filterfrom19to05(data):
	filtered = []
	data = filterWeekends(data)
	for item in data:
		#print(item['date'])
		hour = datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour
		if hour == 19 or hour == 20 or hour == 21 or hour == 22 or hour == 23 or hour == 0 or hour == 1 or hour == 2 or hour == 3 or hour == 4 or hour == 5:
			filtered.append(item)
	#print(filtered)
	return filtered

def filterByLowestByDate(data):
    filtered = []
    day = []
    currentDay = 0
    for item in data:
        itemDay = datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').day
        if itemDay != currentDay and currentDay != 0:
            filtered.append(min(day))
            day = []
        currentDay = itemDay
        day.append(item['spot'])
    print(filtered)
    return filtered
