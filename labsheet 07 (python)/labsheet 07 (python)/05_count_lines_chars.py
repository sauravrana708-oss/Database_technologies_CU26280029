import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 5: Count the number of lines and characters in a file
try:
    with open("sample.txt", "r") as f:
        text = f.read()
    lines = text.split("\n")
    if lines and lines[-1] == "":           # last khali element hatao
        lines.pop()
    print("Total lines     :", len(lines))
    print("Total characters:", len(text))
except FileNotFoundError:
    print("File not found.")
