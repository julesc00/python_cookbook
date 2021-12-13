"""
Problem:
    You want to eliminate the duplicate values in a sequence, but preserve the
    order of the remaining items.

Solution:
    If the values in the sequence are hashable (list or tuple, the problem can be easily solved
    using a set and a generator.
"""

a = [1, 5, 2, 1, 9, 1, 5, 10]


def deduplicate_hashable(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def deduplicate_non_hashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [
    {"x": 1, "y": 2},
    {"x": 1, "y": 3},
    {"x": 1, "y": 2},
    {"x": 2, "y": 4}
]

print(list(deduplicate_hashable(a)))
print(list(deduplicate_non_hashable(b, key=lambda d: (d["x"], d["y"]))))
print(list(deduplicate_non_hashable(b, key=lambda d: d["x"])))

# For lists or tuples if you want to eliminate duplicates, create a set()
lst = set([1, 5, 2, 1, 9, 1, 5, 10])
print(lst)

