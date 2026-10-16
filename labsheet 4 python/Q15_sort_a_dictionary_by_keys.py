# Q15: Sort a dictionary by keys
data = {"banana": 3, "apple": 5, "cherry": 2}
sorted_data = {key: data[key] for key in sorted(data)}
print("Dictionary sorted by keys:", sorted_data)
