"""
3.4. Working with binary, octal and hexadecimal integers

Problem
    You need to convert or output integers represented by binary, octal, or hexadecimal
    digits.
Solution
    To convert an integer into a binary, octal, or hexadecimal text string, use the bin(),
    oct(), or hex() functions, respectively:
"""

X = 1234


def convert_nums_diff():
    print(bin(X))  # 0b10011010010
    print(oct(X))  # 0o2322
    print(hex(X))  # 0x4d2
    print("*" * 20)


def convert_w_format():
    print(format(X, "b"))
    print(format(X, "o"))
    print(format(X, "x"))
    print("*" * 20)


def convert_neg_nums():
    neg_x = -1234
    print(format(2**32 + neg_x, "b"))  # 11111111111111111111101100101110
    print(format(2**32 + neg_x, "x"))  # fffffb2e
    print("*" * 20)


def convert_str_to_ints():
    print(int("4d2", 16))  # 1234
    print(int("10011010010", 2))  # 1234
    print("*" * 20)


"""
Discussion
    For the most part, working with binary, octal, and hexadecimal integers is straightforward.
    Just remember that these conversions only pertain to the conversion of integers
    to and from a textual representation. Under the covers, there’s just one integer type.
    Finally, there is one caution for programmers who use octal. The Python syntax for
    specifying octal values is slightly different than many other languages. For example, if
    you try something like this, you’ll get a syntax error:
    
>>> import os
>>> os.chmod('script.py', 0755)
File "<stdin>", line 1
os.chmod('script.py', 0755)
^
SyntaxError: invalid token
>>>

Make sure you prefix the octal value with 0o, as shown here:
>>> os.chmod('script.py', 0o755)
>>>
"""


if __name__ == "__main__":
    convert_nums_diff()
    convert_w_format()
    convert_neg_nums()
    convert_str_to_ints()
