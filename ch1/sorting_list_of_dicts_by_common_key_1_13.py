"""
Problem
    You have a list of dictionaries and you would like to sort the entries according to one
    or more of the dictionary values.

Solution
    Sorting this type of structure is easy using the operator module’s itemgetter function.
"""

from pprint import PrettyPrinter
from operator import itemgetter

pp = PrettyPrinter(indent=2)

ROWS = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_fname = sorted(ROWS, key=itemgetter("fname"))
rows_by_fname2 = sorted(ROWS, key=lambda r: r["fname"])  # Same as above, but itemgetter() works faster

rows_by_uid = sorted(ROWS, key=itemgetter("uid"))
rows_by_uid2 = sorted(ROWS, key=lambda r: r["uid"])  # Same as above

pp.pprint(rows_by_fname)
pp.pprint(rows_by_uid)

# The itemgetter() function can also accept multiple keys
rows_by_lfname = sorted(ROWS, key=itemgetter("lname", "fname"))
pp.pprint(rows_by_lfname)

# with min() and max()
smallest_id = min(ROWS, key=itemgetter("uid"))
print(smallest_id)
highest_id = max(ROWS, key=itemgetter("uid"))
print(highest_id)
