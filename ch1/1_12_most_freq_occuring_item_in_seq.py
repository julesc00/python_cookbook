"""
Problem:
    You have a sequence of items, and you’d like to determine the most frequently occurring
    items in the sequence.

Solution:
    The collections.Counter class is designed for just such a problem. It even comes with
    a handy most_common() method that will give you the answer.
"""
from pprint import PrettyPrinter
from collections import Counter

pp = PrettyPrinter(indent=2)

WORDS = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(WORDS)
pp.pprint(word_counts)
top_three = word_counts.most_common(3)
pp.pprint(top_three)
print(word_counts["under"])
print(word_counts["eyes"])

# If you want to increment the count manually:
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in more_words:
    word_counts[word] += 1

# Or, alternatively, use the update() method:
word_counts.update(more_words)
pp.pprint(word_counts)

# A little-known feature of Counter instances is that they can be easily combined using
# various mathematical operations.
a = Counter(WORDS)
b = Counter(more_words)
# Combine counts
c = a + b
pp.pprint(c)
# Subtract counts
d = a - b
pp.pprint(d)
