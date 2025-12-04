""" 2025 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = [[int(y) for y in list(x)] for x in f.read().splitlines()]

answer1 = 0
answer2 = 0

for line in input_list:
    if line.index(max(line)) != (len(line) - 1):
        answer1 += int(str(max(line)) + str(max(line[line.index(max(line)) + 1:])))
    else:
        answer1 += int(str(max(line[:-1])) + str(max(line)))

for line in input_list:
    joltage = ""
    prev = 0
    for numbers_left in range(12, 0, -1):
        joltage += str(max(line[prev:len(line) - numbers_left + 1]))
        prev += line[prev:len(line) - numbers_left + 1].index(max(line[prev:len(line) - numbers_left + 1])) + 1
    answer2 += int(joltage)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
