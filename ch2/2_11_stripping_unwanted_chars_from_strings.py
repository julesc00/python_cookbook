"""
2.11. Stripping Unwanted Characters from Strings

Problem
    You want to strip unwanted characters, such as whitespace, from the beginning, end, or
    middle of a text string.

Solution
        The strip() method can be used to strip characters from the beginning or end of a
        string. lstrip() and rstrip() perform stripping from the left or right side,
        respectively.
"""
import re

s = '    hello   world   \n'
print(s.strip())

# Char stripping
t = '-----hello====='
t = t.lstrip("-")
print(t)
t = t.rstrip("=")
print(t)

s2 = '    hello   world   \n'
s2 = s2.replace(" ", "")
s = re.sub("\s+", " ", s)
print(s.strip())
