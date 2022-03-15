"""
2.10. Working with Unicode Characters in Regular Expressions

Problem
    You are using regular expressions to process text, but are concerned about the handling
    of Unicode characters.

Solution
    By default, the re module is already programmed with rudimentary knowledge of certain
    Unicode character classes.
"""
import re

num = re.compile("\d+")
# ASCII digits
print(num.match("123"))  # <re.Match object; span=(0, 3), match='123'>

# Arabic digits
print(num.match('\u0661\u0662\u0663'))  # <re.Match object; span=(0, 3), match='١٢٣'>

# here is a regex that matches all characters in a few different Arabic code pages
arabic = re.compile("[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+")

"""
it’s also
important to be aware of special cases. For example, consider the behavior of case-insensitive
matching combined with case folding
"""
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
print(pat.match(s.upper()))  # Doesn't match, gives None
print(s.upper())  # STRASSE
