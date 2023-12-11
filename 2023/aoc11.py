""" 2023 aoc11 """

with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

lines = set()
rows = set()
galaxies = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "#":
            galaxies[i, j] = char
            lines.add(i)
            rows.add(j)

empty_lines = [i for i in range(len(input_list)) if i not in lines]
empty_rows = [j for j in range(len(input_list[0])) if j not in rows]

answer1 = 0
answer2 = 0
added = set()
for i, j in galaxies:
    added.add((i, j))
    for x, y in galaxies:
        if (x, y) not in added:
            answer1 += abs(x - i) + abs(j - y)
            answer2 += abs(x - i) + abs(j - y)
            for line in empty_lines:
                if min(i, x) < line < max(i, x):
                    answer1 += 1
                    answer2 += 999999
            for row in empty_rows:
                if min(j, y) < row < max(j, y):
                    answer1 += 1
                    answer2 += 999999
print("Answer 1:", answer1)
print("Answer 2:", answer2)
