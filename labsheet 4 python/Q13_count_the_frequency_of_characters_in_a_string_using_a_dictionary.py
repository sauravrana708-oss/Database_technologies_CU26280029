# Q13: Count frequency of characters in a string using a dictionary
text = input("Enter a string: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
print("Character frequency:", frequency)
