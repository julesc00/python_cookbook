"""
2.7. Specifying a Regular Expression for the Shortest Match
Problem
    You’re trying to match a text pattern using regular expressions, but it is identifying
    the longest possible matches of a pattern. Instead, you would like to change it to find
    the shortest possible match.

Solution
    This problem often arises in patterns that try to match text enclosed inside a pair of
    starting and ending delimiters (e.g., a quoted string).
"""
import re

str_pat = re.compile(r"\'(.*)\'")
txt1 = "Computer says 'no.'"
print(str_pat.findall(txt1))  # ['no.']

txt2 = "Computer says 'no.' Phone says 'yes.'"
print(str_pat.findall(txt2))  # ["no.' Phone says 'yes."]
