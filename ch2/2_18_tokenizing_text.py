"""
Problem
    You have a string that you want to parse left to right into a stream of tokens.

Solution
    Suppose you have a string of text such as this:
        text = 'foo = 23 + 42 * 10'

    To tokenize the string, you need to do more than merely match patterns. You need to
    have some way to identify the kind of pattern as well. For instance, you might want to
    turn the string into a sequence of pairs like this:
        tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
        ('NUM', '42'), ('TIMES', '*'), ('NUM', 10')]
"""
import re
from collections import namedtuple

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.search("foo = 42")
print(scanner)


"""
To take this technique and put it into code, it can be cleaned up and easily packaged
into a generator like this:
"""
Token = namedtuple("Token", ["type", "value"])


def generate_tokens(pat, text):
    scanner2 = pat.scanner(text)
    for m in iter(scanner2.match, None):
        yield Token(m.lastgroup, m.group)


for tok in generate_tokens(master_pat, "foo = 42"):
    print(tok)
