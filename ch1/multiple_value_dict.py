
from collections import defaultdict, OrderedDict
import json


d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
d["a"].append(3)
d["a"].append(1)
print(d)


d2 = defaultdict(set)  # Set don't allow duplicates.
d2["a"].add(1)
d2["a"].add(2)
d2["a"].add(1)
print(d2)


d3 = {}
d3.setdefault("a", []).append(1)
d3.setdefault("a", []).append(2)
d3.setdefault("b", []).append(3)
d3.setdefault("a", []).append(2)
print(d3)


# messier code  to create a dict with a list inside
pairs = [("one", 1), ("two", 2)]
d5 = {}
for key, value in pairs:
    if key not in d5:
        d5[key] = []
    d5[key].append(value)


# creating a dict with a list, cleaner code
d4 = defaultdict(list)
for key, value in pairs:
    d4[key].append(value)

print(d4)  # {'one': [1], 'two': [2]})


# An ordered dictionary can be particularly useful when you want to build a mapping that you may want
# to later serialize or encode into a different format.
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for k in d:
    print(k, d[k])


print(json.dumps(d))

