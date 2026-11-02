# Program 7: Write multiple lines of user input into a file
try:
    n = int(input("Kitni lines likhni hain? "))
    with open("user_input.txt", "w") as f:
        for i in range(n):
            f.write(input(f"Line {i + 1}: ") + "\n")
    print("Data saved in user_input.txt")
except ValueError:
    print("Please enter a valid number.")
except IOError as e:
    print("Error:", e)
