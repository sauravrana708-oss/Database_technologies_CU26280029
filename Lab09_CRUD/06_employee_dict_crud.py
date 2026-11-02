# Program 6: CRUD operations on a dictionary of employee data
# Example I/O:
#   Output: step-by-step Create / Read / Update / Delete messages

employees = {101: {"name": "Amit", "salary": 30000},
             102: {"name": "Sita", "salary": 40000}}

# CREATE
employees[103] = {"name": "Ravi", "salary": 35000}
print("Created employee 103")

# READ
for emp_id, info in employees.items():
    print(emp_id, info)

# UPDATE
employees[101]["salary"] = 45000
print("Updated salary of 101:", employees[101])

# DELETE
del employees[102]
print("Deleted employee 102")
print("Final data:", employees)
