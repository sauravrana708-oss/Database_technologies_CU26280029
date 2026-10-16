# Q03: Remove all negative numbers from a list
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
result = [number for number in numbers if number >= 0]
print("List without negative numbers:", result)
