import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 14: Display the longest line in a file
try:
    with open("sample.txt", "r") as f:
        lines = [line.strip() for line in f]
    longest = max(lines, key=len)           # length ke basis par max
    print("Longest line:", longest, f"({len(longest)} characters)")
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("File is empty.")
