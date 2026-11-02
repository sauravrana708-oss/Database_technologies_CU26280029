import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 9: Copy the contents of one file into another
try:
    with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
        dst.write(src.read())               # source ka data destination me
    print("Contents copied from sample.txt to copy.txt")
except FileNotFoundError:
    print("Source file not found.")
