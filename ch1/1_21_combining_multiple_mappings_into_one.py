"""
Problem
    You have multiple dictionaries or mappings that you want to logically combine into a
    single mapping to perform certain operations, such as looking up values or checking
    for the existence of keys.

Solution
    An easy way to do this is to use the ChainMap class from the collections module.
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c["x"])  # Outputs 1 from a
print(c["y"])  # Outputs 2 from b
print(c["z"])  # Outputs 3 from a; if found in the first dict yes else in the next one.
print(len(c))
print(list(c.values()))

# Operations that mutate the mapping always affect the first mapping listed.
c["z"] = 10
c["w"] = 40
del c["x"]
print(c)
print(a)

values = ChainMap()
values["x"] = 1
print(values)

# Add a new mapping
values = values.new_child()
values["x"] = 2
print(values)

values = values.new_child()
values["x"] = 3
print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})

# Discard last mapping
values = values.parents
print(values)  # ChainMap({'x': 2}, {'x': 1})

values = values.parents
print(values)  # ChainMap({'x': 1})


"""
As an alternative to ChainMap, you might consider merging dictionaries together using
the update() method.
"""
d = {"x": 1, "z": 3}
e = {"y": 2, "z": 4}
merged_dicts = dict(e)
merged_dicts.update(d)
print(merged_dicts)  # {'y': 2, 'z': 3, 'x': 1}
print(merged_dicts.get("x", ""))
print(merged_dicts.get("y", ""))
print(merged_dicts.get("z", ""))
d["x"] = 13  # If any of the original dicts mutate, changes don't get reflected.
print(merged_dicts)  # {'y': 2, 'z': 3, 'x': 1}

# A ChainMap uses teh original dicts, so it doesn't have this behavior.
merged_chain_map = ChainMap(d, e)
print(merged_chain_map)  # ChainMap({'x': 13, 'z': 3}, {'y': 2, 'z': 4})
