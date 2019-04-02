class RainfallTable:
	years = dict()
	first_year = int
	last_year  = int

	def __init__(self, filepath):
		data = open(filepath, "r")
		for year in data:
			year_record = self.make_year_tuple(year)
			self.years[year_record[0]] = year_record[1]
		data.close()
		self.first_year = min(self.years.keys())
		self.last_year  = max(self.years.keys())

	def make_year_tuple(self, year_line):
		tokens = year_line.split()
		year = int(tokens[0])
		rainfall = [float (x) for x in tokens[1:]]
		return (year, rainfall)

	def get_rainfall(self, year, month):
		if year not in self.years:
			raise ValueError("Invalid year value.")
		elif month < 1 or month > 12:
			raise ValueError("Invalid month value.")
		else:
			return (self.years[year][month-1])

	def get_min_year(self):
		return self.first_year

	def get_max_year(self):
		return self.last_year

	def get_average_rainfall_for_month(self, month):
		if month < 1 or month > 12:
			raise ValueError("Invalid month value.")
		else:
			all_years = [self.years[y][month-1] for y in self.years]
			return sum(all_years)/len(all_years)

	def get_median_rainfall_for_month(self, month):
		if month < 1 or month > 12:
			raise ValueError("Invalid month value.")
		else:
			median = [self.years[y][month-1] for y in self.years]
			self.sort(median)
			return (median[5] + median[6])/2

	def get_average_rainfall_for_year(self, year):
		if year not in self.years:
			raise ValueError("Invalid year value.")
		else:
			all_months = [self.years[year][m] for m in range(0,12)]
			return sum(all_months)/12

	def get_median_rainfall_for_year(self, year):
		if year not in self.years:
			raise ValueError("Invalid year value.")
		else:
			median = [self.years[year][m] for m in range(0,12)]
			self.sort(median)
			return (median[5] + median[6])/2

	def sort(self, arr):
		for i in range(1, len(arr)):
			key = arr[i]
			j = i-1
			while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
				arr[j+1] = key
		"""
			print ("Sorted array is:")
			for i in range(len(arr)):
				print ("%d" %arr[i])
		"""

	def get_all_by_year(self, year):
		if year not in self.years:
			raise ValueError("Invalid year value.")
		else:
			for i in range(0,12):
				yield (self.years[year][i])

	def get_all_by_month(self, month):
		if month < 1 or month > 12:
			raise ValueError("Invalid month value.")
		else:
			for year in self.years:
				yield (self.years[year][month-1])
				
				

table = RainfallTable("../../data/njrainfall.txt")
print(table.get_rainfall(1993, 6))
print(table.get_average_rainfall_for_month(6))

for year in range(table.get_min_year(), table.get_max_year()+1) :
    print("Average rainfall in ", year, "=", table.get_average_rainfall_for_year(year))
    print("Median rainfall in ", year, "=", table.get_median_rainfall_for_year(year))
    print("===========")
    for rain in table.get_all_by_year(year):
        print(rain, end='\t')
    print("\n===========")


for month in range(1, 13) :
    print("Average rainfall in month", month, "=", table.get_average_rainfall_for_month(month))
    print("Median rainfall in month", month, "=", table.get_median_rainfall_for_month(month))
    print("===========")
    for rain in table.get_all_by_month(month):
        print(rain, end='\t')
    print("\n===========")
