# Program 20: Merge two text files into a third file
import os
# Demo ke liye do sample files banao agar nahi hain
for name, text in [("file1.txt", "This is file one.\n"), ("file2.txt", "This is file two.\n")]:
    if not os.path.exists(name):
        with open(name, "w") as f:
            f.write(text)
try:
    with open("merged.txt", "w") as out:
        for name in ["file1.txt", "file2.txt"]:
            with open(name, "r") as f:
                out.write(f.read())
    print("Files merged into merged.txt")
except FileNotFoundError as e:
    print("Error:", e)
