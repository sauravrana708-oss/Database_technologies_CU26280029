# Q12: Find maximum and minimum marks from a dictionary (without max/min)
students = {"Aman": 78, "Riya": 92, "Karan": 65}
if students:
    names = list(students.keys())
    highest_name = lowest_name = names[0]
    for name in names[1:]:
        if students[name] > students[highest_name]:
            highest_name = name
        if students[name] < students[lowest_name]:
            lowest_name = name
    print("Maximum marks:", students[highest_name], "by", highest_name)
    print("Minimum marks:", students[lowest_name], "by", lowest_name)
else:
    print("Dictionary is empty.")
