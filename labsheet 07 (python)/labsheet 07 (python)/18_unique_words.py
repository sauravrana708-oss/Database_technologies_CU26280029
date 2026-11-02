import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 18: Store only unique words into another file
try:
    with open("sample.txt", "r") as f:
        words = f.read().lower().split()
    unique = list(dict.fromkeys(words))     # duplicates hatao, order same rakho
    with open("unique_words.txt", "w") as f:
        f.write("\n".join(unique))
    print("Unique words saved:", unique)
except FileNotFoundError:
    print("File not found.")
