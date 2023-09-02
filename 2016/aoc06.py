""" 2016 aoc06 """
from collections import Counter

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

letter_counter = []

for x in range(8):
    letter_counter.append("")

for x in input_list:
    for index, y in enumerate(x):
        letter_counter[index] += y

print("Answer 1: ", end="")
for x in letter_counter:
    c = Counter(x)
    for key in reversed(sorted(c, key=c.get)):
        print(key, end="")
        break

print()
print("Answer 2: ", end="")
for x in letter_counter:
    c = Counter(x)

    for key in sorted(c, key=c.get):
        print(key, end="")
        break
