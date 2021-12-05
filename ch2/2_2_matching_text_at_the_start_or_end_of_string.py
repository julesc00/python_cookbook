"""
2.2. Matching Text at the Start or End of a String
Problem
    You need to check the start or end of a string for specific text patterns, such as filename
    extensions, URL schemes, and so on.

Solution
    A simple way to check the beginning or end of a string is to use the str.starts
    with() or str.endswith() methods.
"""
import os
import re
from urllib.request import urlopen

filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

url = "https://www.python.org"
print(url.startswith("https:"))  # True


"""
If you need to check against multiple choices, simply provide a tuple of possibilities to
startswith() or endswith():
"""
filenames = os.listdir(".")
print(filenames)
any(name.endswith(".py") for name in filenames)  # True


def read_data(name):
    if name.startswith("http:", "https:", "ftp:"):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


"""
Oddly, this is one part of Python where a tuple is actually required as input. If you happen
to have the choices specified in a list or set, just make sure you convert them using
tuple() first.
"""
choices = ["http:", "ftp:"]
url = "http://www.python.org"
print(url.startswith(tuple(choices)))  # True


# Prefix or suffix checking
print(url[:5] == "http:" or url[:6] == "https:" or url[:4] == "ftp:")  # True

# Using regex as an alternative
print(re.match("http:|https:|ftp:", url))  # <re.Match object; span=(0, 5), match='http:'>
