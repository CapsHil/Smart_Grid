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
	#print(filtered)

        return filtered

def filterfrom19to05(data):
        filtered = []
        for item in data:
                #print(item['date'])
                hour = datetime.strptime(item['date'], '%m-%d-%Y %H:%M:%S').hour
                if hour == 19 or hour == 20 or hour == 21 or hour == 22 or hour == 23 or hour == 00 or hour == 01 or hour == 02 or hour == 03 or hour == 04 or hour == 05:
                        filtered.append(item)
        #print(filtered)
        return filtered
