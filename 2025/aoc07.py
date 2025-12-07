""" 2025 aoc07 """

with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

start = (0, 0)
beams = set()
splitters = set()
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "^":
            splitters.add((i, j))
        if char == "S":
            start = (i, j)

beams.add(start)
for _ in range(len(input_list)):
    temp = set()
    for x, y in beams:
        if (x + 1, y) in splitters:
            answer1 += 1
            temp.add((x + 1, y + 1))
            temp.add((x + 1, y - 1))
        else:
            temp.add((x + 1, y))
    beams = temp

beams = {start: 1}
for i in range(len(input_list)):
    temp_beams = {}
    for (x, y), v in beams.items():
        if (x + 1, y) in splitters:
            if (x + 1, y + 1) in temp_beams:
                temp_beams[(x + 1, y + 1)] += v
            else:
                temp_beams[(x + 1, y + 1)] = v
            if (x + 1, y - 1) in temp_beams:
                temp_beams[(x + 1, y + 1)] += v
            else:
                temp_beams[(x + 1, y - 1)] = v
        else:
            if (x + 1, y) in temp_beams:
                temp_beams[(x + 1, y)] += v
            else:
                temp_beams[(x + 1, y)] = v
    beams = temp_beams

for k, v in beams.items():
    answer2 += v

print("Answer 1:", answer1)
print("Answer 2:", answer2)
