# Q08: Find pairs whose sum equals a given number
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
target = float(input("Enter target sum: "))
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
print("Pairs:", pairs)
