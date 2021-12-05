"""
2.1. Splitting Strings on Any of Multiple Delimiters
Problem
    You need to split a string into fields, but the delimiters (and spacing around them) aren’t
    consistent throughout the string.

Solution
    The split() method of string objects is really meant for very simple cases, and does
    not allow for multiple delimiters or account for possible whitespace around the delimiters.
    In cases when you need a bit more flexibility, use the re.split() method.
"""
import re

line = 'asdf fjdk; afed, fjek,asdf,   foo'
formatted_list = re.split(r"[;,\s]\s*", line)
print(formatted_list)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


"""
When using re.split(), you need to be a bit careful should the regular expression
pattern involve a capture group enclosed in parentheses. If capture groups are used,
then the matched text is also included in the result.
"""
fields = re.split(r"(;|,|\s)\s*", line)
print(fields)  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fields[::2]
print(values)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimitters = fields[1::2] + [""]
print(delimitters)  # [' ', ';', ',', ',', ',', '']
# Reform the line using the same delimitters.
original_line = "".join(v+d for v, d in zip(values, delimitters))
print(original_line)  # asdf fjdk;afed,fjek,asdf,foo

"""
If you don’t want the separator characters in the result, but still need to use parentheses
to group parts of the regular expression pattern, make sure you use a noncapture group,
specified as (?:...).
"""
formatted_list_again = re.split(r"(?:,|;|\s)\s*", line)
print(formatted_list_again)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
