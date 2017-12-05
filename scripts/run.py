import parseCosts
import filter

def run():
	costsSum = 0
	filtered = filter.filter(parseCosts.parse(), 19)
	for item in filtered:
		costsSum += float(item['spot'])
	print(costsSum*6/1000)
run()
