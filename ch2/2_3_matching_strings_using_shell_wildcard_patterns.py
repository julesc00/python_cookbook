"""
2.3. Matching Strings Using Shell Wildcard Patterns
Problem
    You want to match text using the same wildcard patterns as are commonly used when
    working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

Solution
    The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that
    can be used to perform such matching.
"""
from fnmatch import fnmatch, fnmatchcase

print(fnmatch("foo.txt", "*.txt"))  # True

print(fnmatch("foo.txt", "?oo.txt"))  # True

print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, "Dat*.csv")])  # ['Dat1.csv', 'Dat2.csv']

# On OS X Mac or Windows this matters so instead use fnmatchcase
print(fnmatchcase("foo.txt", "*.TXT"))


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, "* ST")])
# ['5412 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, "54[0-9][0-9] *CLARK*")])
