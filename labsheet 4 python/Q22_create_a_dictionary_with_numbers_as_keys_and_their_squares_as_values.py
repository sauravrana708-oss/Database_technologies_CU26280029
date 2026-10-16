# Q22: Create a dictionary with numbers as keys and squares as values
n = int(input("Enter n: "))
squares = {number: number ** 2 for number in range(1, n + 1)}
print("Number-square dictionary:", squares)
