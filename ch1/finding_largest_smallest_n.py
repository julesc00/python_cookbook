"""
you want to make a list of the largest or smallest N items in a collection.
heapq: has nlargest() or nsmallest()
"""

import heapq
import pprint

pp = pprint.PrettyPrinter(indent=3, sort_dicts=True)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nums)
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
pp.pprint(cheap)
