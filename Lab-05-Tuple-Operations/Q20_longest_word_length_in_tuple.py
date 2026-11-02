"""Lab solution: Longest Word Length in Tuple
Question number: 20
"""

words = tuple(input("Enter words separated by spaces: ").split())
print("Longest word length:", max((len(word) for word in words), default=0))
