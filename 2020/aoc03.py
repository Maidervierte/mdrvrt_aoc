""" 2020 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

trees = {}

for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        trees[(i, j)] = char

answer1 = 0
cur_pos = (0, 0)
while cur_pos in trees:
    if trees[cur_pos] == "#":
        answer1 += 1
    cur_pos = (cur_pos[0] + 1, cur_pos[1] + 3)
    if cur_pos[1] >= len(input_list[0]):
        cur_pos = (cur_pos[0], cur_pos[1] - len(input_list[0]))

print("Answer 1:", answer1)

answer2 = answer1
for slope in [(1, 1), (5, 1), (7, 1), (1, 2)]:
    cur_pos = (0, 0)
    temp = 0
    while cur_pos in trees:
        if trees[cur_pos] == "#":
            temp += 1
        cur_pos = (cur_pos[0] + slope[1], cur_pos[1] + slope[0])
        if cur_pos[1] >= len(input_list[0]):
            cur_pos = (cur_pos[0], cur_pos[1] - len(input_list[0]))
    answer2 *= temp

print("Answer 2:", answer2)
