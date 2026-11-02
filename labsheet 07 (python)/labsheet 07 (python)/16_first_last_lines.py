import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 16: Display the first and last lines of a file
try:
    with open("sample.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]   # khali lines ignore
    if lines:
        print("First line:", lines[0])
        print("Last line :", lines[-1])
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found.")
