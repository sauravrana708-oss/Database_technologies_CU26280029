# Q30: Create a dictionary of character frequencies in a string
text = input("Enter a string: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
print("Character frequency:", frequency)
