# Q16: Sort a dictionary by values
data = {"Aman": 78, "Riya": 92, "Karan": 65}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_data)
