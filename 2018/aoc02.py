""" 2018 aoc02 """
from collections import Counter

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

twos = 0
threes = 0
for x in input_list:
    c = Counter(x)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1
print("Answer 1:", twos * threes)
print("Answer 2: ", end="")
for index1, x in enumerate(input_list):
    for index2, y in enumerate(input_list):
        if index1 != index2 and len(set(x).difference(set(y))) == 1:
            diff = 0
            for i1, a in enumerate(x):
                for i2, b in enumerate(y):
                    if i1 == i2 and a != b:
                        diff += 1
            if diff == 1:
                for i1, a in enumerate(x):
                    for i2, b in enumerate(y):
                        if i1 == i2 and a == b:
                            print(a, end="")
