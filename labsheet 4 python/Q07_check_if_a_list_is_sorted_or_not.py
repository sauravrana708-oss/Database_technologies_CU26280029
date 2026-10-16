# Q07: Check if a list is sorted or not
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
is_sorted = True
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        is_sorted = False
        break
print("The list is sorted." if is_sorted else "The list is not sorted.")
