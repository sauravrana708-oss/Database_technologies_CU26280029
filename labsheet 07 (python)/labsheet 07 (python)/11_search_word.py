import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 11: Search for a particular word in a file
try:
    word = input("Enter word to search: ").lower()
    found = False
    with open("sample.txt", "r") as f:
        for number, line in enumerate(f, start=1):
            if word in line.lower():
                print(f"Found in line {number}: {line.strip()}")
                found = True
    if not found:
        print("Word not found.")
except FileNotFoundError:
    print("File not found.")
