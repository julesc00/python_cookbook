"""
Problem:
    Your program has become an unreadable mess of hardcoded slice indices and you want
    to clean it up.

Solution:
    Naming slices
"""

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
del items[a]
print(items)

b = slice(10, 50, 2)
print(b.start)
print(b.stop)
print(b.step)


# you can map a slice onto a sequence of a specific size by using its
# indices(size) method.
s = "HelloWorld"
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
