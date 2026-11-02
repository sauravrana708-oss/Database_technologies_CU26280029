import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 10: Read a file and convert its content to uppercase
try:
    with open("sample.txt", "r") as f:
        upper_text = f.read().upper()       # upper() sab capital kar deta hai
    print(upper_text)
    with open("upper.txt", "w") as f:       # result alag file me save
        f.write(upper_text)
except FileNotFoundError:
    print("File not found.")
