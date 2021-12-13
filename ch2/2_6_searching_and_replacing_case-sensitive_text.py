"""
2.6. Searching and Replacing Case-Insensitive Text
Problem
    You need to search for and possibly replace text in a case-insensitive manner.

Solution
    To perform case-insensitive text operations, you need to use the re module and supply
    the re.IGNORECASE flag to various operations.
"""
import re

text = "UPPER PYTHON, lower python, Mixed Python"
py_search = re.findall("python", text, flags=re.IGNORECASE)
print(py_search)

sub_py_for_snake = re.sub("python", "snake", text, flags=re.IGNORECASE)
print(sub_py_for_snake)


def match_case(word):
    """
    The last example reveals a limitation that replacing text won’t match the case of the
    matched text. If you need to fix this, you might have to use a support function,
    as in the following:
    """
    def replace(m):
        txt = m.group()
        if txt.isupper():
            return word.upper()
        elif txt.islower():
            return word.lower()
        elif txt.istitle():
            return word.title()
        else:
            return word
    return replace


