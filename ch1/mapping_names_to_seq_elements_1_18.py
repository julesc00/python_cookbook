"""
1.18. Mapping Names to Sequence Elements
Problem
    You have code that accesses list or tuple elements by position, but this makes the code
    somewhat difficult to read at times. You’d also like to be less dependent on position in
    the structure, by accessing the elements by name.

Solution
    collections.namedtuple() provides these benefits, while adding minimal overhead
    over using a normal tuple object. collections.namedtuple() is actually a factory
    method that returns a subclass of the standard Python tuple type. You feed it a type
    name, and the fields it should have, and it returns a class that you can instantiate,
    passing in values for the fields you’ve defined, and so on.

    it should be noted that if your goal is to define an efficient data
    structure where you will be changing various instance attributes, using namedtuple is
    not your best choice. Instead, consider defining a class using __slots__ instead
"""

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("julito@chulito.com", "2021-10-12")
print(sub)
print(sub.addr)
print(sub.joined)


"""
A major use case for named tuples is decoupling your code from the position of the
elements it manipulates. So, if you get back a large list of tuples from a database call,
then manipulate them by accessing the positional elements, your code could break if,
say, you added a new column to your table. Not so if you first cast the returned tuples
to namedtuples.
"""


# Not so nice
def compute_cost(records):
    total = 0.0
    total += (rec[1] * rec[2] for rec in records)
    return total


# Nicer with namedtuple
Stock = namedtuple("Stock", ["shares", "price"])
stocks = [(10, 20), (30, 30), (540, 323)]


def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


print(compute_cost2(stocks))  # 175520.0

Stock2 = namedtuple("Stock", ["name", "shares", "price", "date", "time"])

# Create a prototype instance
stock_prototype = Stock2("", 0, 0.0, None, None)
print(stock_prototype)


# Function to convert a dict to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {"name": "ACME", "shares": 100, "price": 123.53}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
