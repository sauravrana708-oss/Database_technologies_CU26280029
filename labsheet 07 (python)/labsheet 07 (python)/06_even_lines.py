import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 6: Display only even-numbered lines from a file
try:
    with open("sample.txt", "r") as f:
        for number, line in enumerate(f, start=1):   # line number 1 se start
            if number % 2 == 0:
                print(number, ":", line.strip())
except FileNotFoundError:
    print("File not found.")
