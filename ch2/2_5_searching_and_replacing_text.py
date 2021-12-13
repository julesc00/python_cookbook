"""
2.5. Searching and Replacing Text
Problem
    You want to search for and replace a text pattern in a string.

Solution
    For simple literal patterns, use the str.replace() method.
    For more complicated patterns, use the sub() functions/methods in the re module.
"""
import re
from calendar import month_abbr


text = "yeah, but no, but yeah, but no, but yeah"
print(text.replace("yeah", "yep"))

text2 = "Today is 11/27/2012. PyCon starts 3/13/2013."
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text2))


"""
If you’re going to perform repeated substitutions of the same pattern, consider 
compiling it first for better performance.
"""
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
print(datepat.sub(r"\3-\1-\2", text2))


def change_date(m):
    """
    For more complicated substitutions, it’s possible to specify a substitution
    callback function instead.
    """
    month_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {month_name} {m.group(3)}"


print(datepat.sub(change_date, text2))

new_text, n = datepat.subn(r"\3-\1-\2", text2)
print(new_text, n)
