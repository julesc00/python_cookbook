
"""
1.1 You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
"""

p = (4, 5)
x, y = p

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

# Discarding items
_, shares2, _, date2 = data
print(shares2, date2)


"""
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
"""


def drop_first_last(grades):
    """Find the average grade."""
    first, *middle, last = grades
    return sum(middle) / len(middle)


print(drop_first_last([60, 86, 100, 100, 90, 75, 95]))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
first_name, email, *phone_nums = record
