import os
# Numbers wali sample file banao agar nahi hai
if not os.path.exists("numbers.txt"):
    with open("numbers.txt", "w") as f:
        f.write("10\n20\n30\n40\n50\n")

# Program 13: Read numbers from a file and display their sum and average
try:
    with open("numbers.txt", "r") as f:
        numbers = [float(line) for line in f if line.strip()]   # khali lines skip
    if numbers:
        print("Sum    :", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("File contains non-numeric data.")
