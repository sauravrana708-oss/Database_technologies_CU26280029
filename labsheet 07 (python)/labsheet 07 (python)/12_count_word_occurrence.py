import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 12: Count the occurrence of a specific word in a file
try:
    word = input("Enter word to count: ").lower()
    with open("sample.txt", "r") as f:
        words = f.read().lower().split()
    print(f"'{word}' appears {words.count(word)} time(s).")
except FileNotFoundError:
    print("File not found.")
