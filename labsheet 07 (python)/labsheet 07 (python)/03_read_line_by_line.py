import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 3: Read a file line by line
try:
    with open("sample.txt", "r") as f:
        for line in f:                      # file object ko loop me use karo
            print(line.strip())             # strip() newline hata deta hai
except FileNotFoundError:
    print("File not found.")
