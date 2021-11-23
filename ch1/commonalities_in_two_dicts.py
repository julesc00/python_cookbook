"""
Problem:
    you have two dictionaries and want to find out what they have in common (same
    keys, same values, etc.).

Solution:
    To find out what the two dictionaries have in common, simply perform common
    set operations using the keys() or items() methods.
"""


a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}

# Find keys in common
print(a.keys() & b.keys())  # {'x', 'y'}

# Find keys in a that are not in b
print(a.keys() - b.keys())  # {'z'}

# Find (key, value) pairs in common
print(a.items() & b.items())  # {('y', 2)}

# Make a new dictionary with certain removed keys:
c = {key: a[key] for key in a.keys() - {"z", "w"}}
print(c)  # {'x': 1, 'y': 2}
