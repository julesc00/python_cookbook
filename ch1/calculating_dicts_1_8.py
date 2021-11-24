"""
Problem:
    You want to perform various calculations (eg. minimum value, max value, sorting, etc.

Solution:
    Consider a dictionary that maps stock names to prices:
"""
import pprint

pp = pprint.PrettyPrinter(indent=2)

PRICES = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75
}

# zip() good to invert key, values in a dict.
min_price = min(zip(PRICES.values(), PRICES.keys()))
max_price = max(zip(PRICES.values(), PRICES.keys()))
print(min_price)
print(max_price)

# zip() creates an generator that can only be consumed once, wrap it in a data structure such a list or tuple
# to make it reusable.
prices_names = list(zip(PRICES.values(), PRICES.keys()))
print(min(prices_names))
print(max(prices_names))

# Similarly, to rank the data use zip() with sorted(), as in the following:
prices_sorted = sorted(zip(PRICES.values(), PRICES.keys()))
pp.pprint(prices_sorted)

# You can get the key corresponding to the min, max value if you supply a key function to min() and max().
print(min(PRICES, key=lambda k: PRICES[k]))
print(max(PRICES, key=lambda k: PRICES[k]))

min_value = PRICES[min(PRICES, key=lambda k: PRICES[k])]
print(min_value)

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Vicky"]
x = list(zip(a, b))
for man, girl in x:
    print(f"{man} loves {girl}!")
