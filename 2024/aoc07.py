""" 2024 aoc07 """
from itertools import product

with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = [[int(x.split(": ")[0]),
                   [int(y) for y in x.split(": ")[1].split(" ")]] for x in f.read().splitlines()]

answer1 = 0
answer2 = 0

for line in input_list:
    for operators in product([0, 1], repeat=len(line[1]) - 1):
        result = line[1][0]
        for i, operator in enumerate(operators):
            if operator == 0:
                result += line[1][i + 1]
            if operator == 1:
                result *= line[1][i + 1]
        if result == line[0]:
            answer1 += line[0]
            break
print("Answer 1:", answer1)

for line in input_list:
    for operators in product([0, 1, 2], repeat=len(line[1]) - 1):
        result = line[1][0]
        for i, operator in enumerate(operators):
            if operator == 0:
                result += line[1][i + 1]
            if operator == 1:
                result *= line[1][i + 1]
            if operator == 2:
                result = int(str(result) + str(line[1][i + 1]))
        if result == line[0]:
            answer2 += line[0]
            break
print("Answer 2:", answer2)
