import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 4: Count the number of words in a text file
try:
    with open("sample.txt", "r") as f:
        words = f.read().split()            # whitespace par split
    print("Total words:", len(words))
except FileNotFoundError:
    print("File not found.")
