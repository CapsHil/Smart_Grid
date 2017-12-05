import parseCosts
import filter

def run():
	print('****************')
	print('****************')
	print('****************')
	print('****************')
	print('PROGRAM START***')
	print('****************')
	print('****************')
	print('****************')
	costsSum = 0
	filtered = filter.filter(parseCosts.parse(), 19)
	for item in filtered:
		print(item)
		costsSum += float(item['spot'])
	print(costsSum*6*0.001)

	print('////////////////')
	print('////////////////')
	print('////////////////')
	print('////////////////')
	print('PROGRAM END/////')
	print('////////////////')
	print('////////////////')
	print('////////////////')


run()
