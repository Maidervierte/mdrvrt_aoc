""" 2017 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

input_lines = [int(x) for x in input_lines]
index = 0
steps = 0
while index < len(input_lines):
    input_lines[index] += 1
    index += input_lines[index] - 1
    steps += 1
print("Answer 1:", steps)

with open("input05.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

input_lines = [int(x) for x in input_lines]
index = 0
steps = 0
while index < len(input_lines):
    if input_lines[index] > 2:
        input_lines[index] -= 1
        index += input_lines[index] + 1
    else:
        input_lines[index] += 1
        index += input_lines[index] - 1
    steps += 1
print("Answer 2:", steps)
