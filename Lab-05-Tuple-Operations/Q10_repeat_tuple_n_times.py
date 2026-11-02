"""Lab solution: Repeat Tuple N Times
Question number: 10
"""

items = tuple(input("Enter tuple items: ").split())
n = int(input("Repeat count: "))
print(items * max(0, n))
