"""
Problem
    You’re trying to match a block of text using a regular expression, but you need the match
    to span multiple lines.

Solution
    This problem typically arises in patterns that use the dot (.) to match any character but
    forget to account for the fact that it doesn’t match newlines.
"""
import re

comment = re.compile(r"/\*(.*?)\*/")
txt1 = "/* this is a comment */"
txt2 = """/* this is a
            multiline comment */
"""
print(comment.findall(txt1))
print(comment.findall(txt2))

comment_new_lines = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment_new_lines.findall(txt2))

# The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes
# the . in a regular expression match all characters, including newlines.

comment3 = re.compile(r"/\*(.*?)\*/", re.DOTALL)
print(comment3.findall(txt2))  # [' this is a\n            multiline comment ']
