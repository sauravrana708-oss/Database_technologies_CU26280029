import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 2: Read the entire content of a text file
try:
    with open("sample.txt", "r") as f:      # "r" mode: sirf padhne ke liye
        content = f.read()                  # poori file ek string me
    print(content)
except FileNotFoundError:
    print("File not found.")
