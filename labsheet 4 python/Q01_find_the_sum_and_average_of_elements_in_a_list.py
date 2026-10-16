# Q01: Find the sum and average of elements in a list
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
if numbers:
    total = sum(numbers)
    print("Sum:", total)
    print("Average:", total / len(numbers))
else:
    print("The list is empty.")
