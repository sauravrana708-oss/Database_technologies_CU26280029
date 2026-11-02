import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 15: Replace a word in a file with another word
try:
    old = input("Word to replace: ")
    new = input("New word: ")
    with open("sample.txt", "r") as f:
        text = f.read()
    with open("sample.txt", "w") as f:      # updated text wapas likho
        f.write(text.replace(old, new))
    print("Replacement done.")
except FileNotFoundError:
    print("File not found.")
