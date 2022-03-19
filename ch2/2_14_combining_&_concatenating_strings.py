"""
2.14
Problem
    You want to combine many small strings together into a larger string.

Solution:
    If the strings you wish to combine are found in a sequence or iterable, the fastest way
    to combine them is to use the join() method.
"""

parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))

a = "Is Chicago"
b = "Not Chicago?"
print(a+" "+b)

print("{} {}".format(a, b))

# If you're trying to combine string literals together in source code, simply place
# them adjacent to each other with no + operator.
c = "Hello" "World"
print(c)

# This could be nice for a CSV format.
data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))

# Be careful with concatenation.
print(a + ":" + b + ":" + c)  # Ugly
print(":".join([a, b, c]))  # Still ugly
print(a, b, c, sep=":")  # Better

"""
If you're writing code that is building output from lots of small strings, you
might consider writing that code as a generator function, using yield to emit fragments.
"""
FRAG = ["hola", "como", "has", "estado", "ultimamente"]


def sample() -> str:
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


text = " ".join(sample())
print(text)


def sample_2(msg: list) -> str:
    for i in msg:
        yield i


text2 = " ".join(sample_2(FRAG))
print(text2.capitalize())
