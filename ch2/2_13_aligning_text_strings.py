"""
Problem
    You need to format text with some sort of alignment applied.

Solution:
    For basic alignment of strings, the ljust(), rjust(), and center() methods of strings can be used.
"""

text = "hello world"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# Optional &&65.18&&fill character as well
print(text.rjust(20, "="))
print(text.ljust(20, "*"))
print(text.center(20, "*"))

# format()
print(format(text, ">20"))
print(format(text, "<20"))
print(format(text, "^20"))

# format() with fill character
print(format(text, "=>20"))
print(format(text, "*<20"))
print(format(text, "*^20"))

print("{:>10s} {:>10s}".format("Hello", "World"))

# With numbers
x = 1.2535
print(format(x, ">10"))
print(format(x, "^10.2f"))
