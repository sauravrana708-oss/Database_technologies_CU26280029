"""Lab solution: Power Set
Question number: 19
"""

items = list(set(input("Enter a small set of items: ").split()))
if len(items) > 15:
    print("Please enter 15 or fewer distinct elements.")
else:
    power_set = []
    for mask in range(1 << len(items)):
        subset = {items[i] for i in range(len(items)) if mask & (1 << i)}
        power_set.append(subset)
    print(power_set)
