# Q25: Count word frequency in a paragraph using a dictionary
import string
paragraph = input("Enter a paragraph: ").lower()
for punctuation in string.punctuation:
    paragraph = paragraph.replace(punctuation, " ")
frequency = {}
for word in paragraph.split():
    frequency[word] = frequency.get(word, 0) + 1
print("Word frequency:", frequency)
