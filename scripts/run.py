import parseCosts
import filter

def run():
	print('****************')
	costsSum = 0
	filtered = filter.filter(parseCosts.parse(), 19)
	for item in filtered:
		print(item)
		costsSum += float(item['spot'])
	print(costsSum*6*0.001)
run()
