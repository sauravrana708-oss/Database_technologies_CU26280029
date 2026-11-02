"""Lab solution: Unzip List of Tuples
Question number: 27
"""

pairs = [(1, "A"), (2, "B"), (3, "C")]
if pairs:
    numbers, letters = zip(*pairs)
    print("First values:", list(numbers))
    print("Second values:", list(letters))
