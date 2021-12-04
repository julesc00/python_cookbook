"""
Problem
    You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
    transform or filter the data.

Solution
    A very elegant way to combine a data reduction and a transformation is to use a
    generator-expression argument.
"""
import os

numbs = [1, 2, 3, 4, 6]
s = [x * x for x in numbs]
print(s)

# Determine in any .py files exist in a dir.
# files = os.listdir("dirname")
# if any(name.endswith(".py") for name in files):
#     print("There be python!")
# else:
#     print("sorry, no python.")

# Output a tuple as CSV
s2 = ("ACME", 50, 123.45)
print(",".join(str(x) for x in s2))  # ACME,50,123.45

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(share["shares"] for share in portfolio)
print(min_shares)

# Alternative to the above reduction
min_shares2 = min(portfolio, key=lambda x: x["shares"])
print(min_shares2)

s3 = sum(x * x for x in numbs)  # More elegant syntax
