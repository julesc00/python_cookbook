
"""
1.1 You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
"""

# p = (4, 5)
# x, y = p
#
# data = ["ACME", 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
#
# # Discarding items
# _, shares2, _, date2 = data
# print(shares2, date2)


"""
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
"""


# def drop_first_last(grades):
#     """Find the average grade."""
#     first, *middle, last = grades
#     return sum(middle) / len(middle)
#
#
# print(drop_first_last([60, 86, 100, 100, 90, 75, 95]))
#
#
# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# first_name, email, *phone_nums = record
#
# records = [
#     ("foo", 1, 2),
#     ("bar", "hello"),
#     ("foo", 3, 4)
# ]
#
#
# def do_foo(x, y):
#     print(f"foo {x}{y}")
#
#
# def do_bar(s: str):
#     print("bar", s)
#
#
# for tag, *args in records:
#     if tag == "foo":
#         do_foo(*args)
#     elif tag == "bar":
#         do_bar(*args)

items_lst = [1, 10, 7, 4, 5, 9]


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items_lst))
