import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 17: Remove blank lines from a file
try:
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    with open("no_blank.txt", "w") as f:
        for line in lines:
            if line.strip():                # sirf non-empty lines likho
                f.write(line)
    print("Blank lines removed. Output saved in no_blank.txt")
except FileNotFoundError:
    print("File not found.")
