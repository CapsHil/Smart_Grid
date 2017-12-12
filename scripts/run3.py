import parseCosts as p
import filter as f
from datetime import datetime

sum = 0
data = f.filterByLowestByDate(f.filterfrom19to05(f.filterWeekends(p.parse())))
for value in data:
    sum += float(value)*6/1000
print(sum)