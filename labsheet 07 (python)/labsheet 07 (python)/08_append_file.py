import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 8: Append new content to an existing file
try:
    new_text = input("Enter text to append: ")
    with open("sample.txt", "a") as f:      # "a" mode: end me add karta hai
        f.write(new_text + "\n")
    print("Content appended successfully.")
except IOError as e:
    print("Error:", e)
