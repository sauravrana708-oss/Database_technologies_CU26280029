"""Lab solution: Anagram Check Using Sets
Question number: 27
"""

a = input("First string: ").replace(" ", "").lower()
b = input("Second string: ").replace(" ", "").lower()
# Sets compare unique characters; frequency is also checked to handle repeated letters.
print("Anagrams" if set(a) == set(b) and sorted(a) == sorted(b) else "Not anagrams")
