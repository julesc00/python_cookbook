"""
2.16. Reformatting Text to a Fixed Number of Columns
Problem
    You have long strings that you want to reformat so that they fill a user-specified
    number of columns.

Solution
    Use the textwrap module to reformat text for output.
"""
import textwrap
import os

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent="    "))
print(textwrap.fill(s, 40, subsequent_indent="    "))
print(os.get_terminal_size().columns)
