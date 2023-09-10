""" 2017 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

answer1 = 0
for line in input_lines:
    if len(line.split(" ")) == len(set(line.split(" "))):
        answer1 += 1
print("Answer 1:", answer1)

answer2 = 0
for line in input_lines:
    line_split = line.split(" ")
    line_split = ["".join(sorted(x)) for x in line_split]
    if len(line_split) == len(set(line_split)):
        answer2 += 1
print("Answer 2:", answer2)
