# Program 1: Create a file and write text into it
try:
    with open("sample.txt", "w") as f:      # "w" mode: file create / overwrite karta hai
        f.write("Python is easy\n")
        f.write("Python is powerful\n")
    print("File created and text written successfully.")
except IOError as e:
    print("Error:", e)
