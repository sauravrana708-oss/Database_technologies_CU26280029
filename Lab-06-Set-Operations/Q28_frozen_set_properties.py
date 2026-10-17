"""Lab solution: Frozen Set Properties
Question number: 28
"""

items = frozenset(input("Enter items separated by spaces: ").split())
print("Frozen set:", items)
print("Length:", len(items))
print("Contains 'a':", "a" in items)
# frozenset is immutable; it has no add() or remove() methods.
