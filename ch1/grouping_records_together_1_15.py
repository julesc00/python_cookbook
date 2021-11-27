"""
Problem
    You have a sequence of dictionaries or instances and you want to iterate over the data
    in groups based on the value of a particular field, such as date.

Solution
    The itertools.groupby() function is particularly useful for grouping data together
    like this.
"""

from operator import itemgetter
from itertools import groupby
from pprint import PrettyPrinter
from collections import defaultdict

pp = PrettyPrinter(indent=4, depth=4)

ROWS = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

ROWS.sort(key=itemgetter("date"))

for date, items in groupby(ROWS, key=itemgetter("date")):
    print(date)
    for i in items:
        print("    ", i)


"""
If your goal is to simply group the data together by dates into a large data structure that
allows random access, you may have better luck using defaultdict() to build a multidict.
"""
rows_by_date = defaultdict(list)
[rows_by_date[row["date"]].append(row) for row in ROWS]
pp.pprint(rows_by_date)

for r in rows_by_date["07/01/2012"]:
    print(r)

