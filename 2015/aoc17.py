""" 2015 aoc17 """
from itertools import combinations

with open("input17.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

input_lines = [int(line) for line in input_lines]

combs = []
for i in range(1, len(input_lines) + 1):
    combs += list(combinations(input_lines, i))

answer1 = 0
min_length = len(input_lines)
for comb in combs:
    if sum(comb) == 150:
        answer1 += 1
        if len(comb) < min_length:
            min_length = len(comb)

min_length_combs = list(combinations(input_lines, min_length))

answer2 = 0
for min_length_comb in min_length_combs:
    if sum(min_length_comb) == 150:
        answer2 += 1
print("Answer 1:", answer1)
print("Answer 1:", answer2)
