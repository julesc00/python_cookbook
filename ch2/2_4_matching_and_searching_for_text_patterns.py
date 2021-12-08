"""
2.4. Matching and Searching for Text Patterns

Problem
    You want to match or search text for a specific pattern.

Solution
    If the text you’re trying to match is a simple literal, you can often just use the basic string
    methods, such as str.find(), str.endswith(), str.startswith(), or similar.
"""
import re

# Exact match, no
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == "yeah")  # False

# Match at start or end
print(text.startswith("yeah"))  # True
print(text.endswith("no"))  # False

# Search for the location of the first occurrence
print(text.find("no"))  # 10

"""
For more complicated matching, use regular expressions and the re module. To illustrate
the basic mechanics of using regular expressions, suppose you want to match dates
specified as digits, such as “11/27/2012.”
"""
text2 = "12/08/2021"
text3 = "Dec 08, 2021"

# Simple matching: \d+ means match one or more digits
if re.match(r"\d+/\d+/\d+", text3):
    print("yes")
else:
    print("no")

"""
If you’re going to perform a lot of matches using the same pattern, it usually pays to
precompile the regular expression pattern into a pattern object first.
"""
date_pat = re.compile(r"\d+/\d+/\d+")
if date_pat.match(text2):
    print("yes")
else:
    print("no")

print("yes") if date_pat.match(text2) else print("no")
print("yes") if date_pat.match(text3) else print("no")

"""
match() always tries to find the match at the start of a string. If you want to search text
for all occurrences of a pattern, use the findall() method instead.
"""
text4 = "Today is 12/08/2021. PyCon starts 3/13/2022."
print(date_pat.findall(text4))

"""
When defining regular expressions, it is common to introduce capture groups by enclosing
parts of the pattern in parentheses.

Capture groups often simplify subsequent processing of the matched text because the
contents of each group can be extracted individually.
"""
date_pat2 = re.compile(r"(\d+)/(\d+)/(\d+)")
m = date_pat2.match("12/08/2022")
print(m)

# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month, day, year = m.groups()
print(month, day, year)

# Find all matches (notice splitting into tuples)
print(date_pat2.findall(text4))
for month, day, year in date_pat2.findall(text4):
    print(f"{year}-{month}-{day}")


"""
The findall() method searches the text and finds all matches, returning them as a list.
If you want to find matches iteratively, use the finditer() method instead.
"""
for m in date_pat2.finditer(text4):
    print(m.groups())

"""
If you want an exact match, make sure the pattern includes the end-marker ($).
"""
date_pat_exact_match = re.compile(r"(\d+)/(\d+)/(\d+)$")
print(date_pat_exact_match.match("11/27/2012abcdef"))
print(date_pat_exact_match.match("11/27/2012"))

"""
Last, if you’re just doing a simple text matching/searching operation, you can often skip
the compilation step and use module-level functions in the re module instead.
"""
print(re.findall(r"(\d+)/(\d+)/(\d+)", text4))
