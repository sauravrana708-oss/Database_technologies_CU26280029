import os
# Sample input file banao agar pehle se nahi hai
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        f.write("Python is easy\nPython is powerful\n\nFile handling in Python\nLearning python is fun\n")

# Program 19: Sort all words alphabetically and save to a new file
try:
    with open("sample.txt", "r") as f:
        words = f.read().lower().split()
    words.sort()                            # alphabetical order
    with open("sorted_words.txt", "w") as f:
        f.write("\n".join(words))
    print("Sorted words:", words)
except FileNotFoundError:
    print("File not found.")
