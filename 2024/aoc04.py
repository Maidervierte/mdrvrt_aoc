""" 2024 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = [list(x) for x in f.read().splitlines()]

answer1 = 0
answer2 = 0

for line in input_list:
    stringline = "".join(line)
    answer1 += stringline.count("XMAS") + stringline[::-1].count("XMAS")

transpose = list(map(list, zip(*input_list)))
for line in transpose:
    stringline = "".join(line)
    answer1 += stringline.count("XMAS") + stringline[::-1].count("XMAS")

visited = set()
for x in range(len(input_list)):
    for y in range(len(input_list[0])):
        temp = input_list[x][y]
        for i in range(1, len(input_list) + len(input_list[0])):
            if x + i >= len(input_list) or y + i >= len(input_list[0]):
                break
            if (x + i, y + i) in visited:
                break
            temp += input_list[x + i][y + i]
            visited.add((x + i, y + i))
        answer1 += temp.count("XMAS") + temp[::-1].count("XMAS")

visited = set()
for x in range(len(input_list)):
    for y in range(len(input_list[0]) - 1, -1, -1):
        temp = input_list[x][y]
        for i in range(1, (len(input_list) + len(input_list[0]))):
            if x + i >= len(input_list) or y - i < 0:
                break
            if (x + i, y - i) in visited:
                break
            temp += input_list[x + i][y - i]
            visited.add((x + i, y - i))
        answer1 += temp.count("XMAS") + temp[::-1].count("XMAS")

print("Answer 1:", answer1)

for x in range(1, len(input_list) - 1):
    for y in range(1, len(input_list[0]) - 1):
        if input_list[x][y] == "A":
            if input_list[x - 1][y - 1] == "M" and input_list[x + 1][y - 1] == "M" \
                    and input_list[x - 1][y + 1] == "S" and input_list[x + 1][y + 1] == "S":
                answer2 += 1
            if input_list[x - 1][y - 1] == "S" and input_list[x + 1][y - 1] == "S" \
                    and input_list[x - 1][y + 1] == "M" and input_list[x + 1][y + 1] == "M":
                answer2 += 1
            if input_list[x - 1][y - 1] == "M" and input_list[x + 1][y - 1] == "S" \
                    and input_list[x - 1][y + 1] == "M" and input_list[x + 1][y + 1] == "S":
                answer2 += 1
            if input_list[x - 1][y - 1] == "S" and input_list[x + 1][y - 1] == "M" \
                    and input_list[x - 1][y + 1] == "S" and input_list[x + 1][y + 1] == "M":
                answer2 += 1

print("Answer 2:", answer2)
