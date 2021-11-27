"""
Problem
    You have data inside of a sequence, and need to extract values or reduce the
    sequence using some criteria.

Solution
    The easiest way to filter sequence data is often to use a list comprehension.
"""
import math
from itertools import compress


my_list = [1, 4, -5, 10, -7, 2, 3, -1]

positive_nums = sorted([n for n in my_list if n > 0])
print(positive_nums)  # [1, 2, 3, 4, 10]

negative_nums = sorted(n for n in my_list if n < 0)
print(negative_nums)  # [-7, -5, -1]

"""
For example, suppose that the filtering process involves exception handling or 
some other complicated detail. For this, put the filtering code into its own
function and use the built-in filter() function.
"""

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
values2 = ["True", "False", "false", "true", 2, 4.20]


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


int_values = list(filter(is_int, values))
print(int_values)  # ['1', '2', '-3', '4', '5']


sqr_nums = [math.sqrt(n) for n in my_list if n > 0]
print(sqr_nums)


"""
perhaps instead of just finding positive values, you want to also clip bad 
values to fit within a specified range.
"""

clip_neg = [n if n > 0 else 0 for n in my_list]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in my_list]
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)
addresses5 = list(compress(addresses, more5))
print(addresses5)

