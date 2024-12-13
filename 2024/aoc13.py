""" 2024 aoc13"""

with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split("\n\n")

answer1 = 0
answer2 = 0

for line in input_list:
    line = line.splitlines()
    x1, y1 = [int(x[2:]) for x in line[0].split(": ")[1].split(", ")]
    x2, y2 = [int(x[2:]) for x in line[1].split(": ")[1].split(", ")]
    px, py = [int(x[2:]) for x in line[2].split(": ")[1].split(", ")]
    min_tokens = 401
    for x in range(100):
        for y in range(100):
            if (x1 * x + x2 * y) == px and (y1 * x + y2 * y) == py:
                cur_tokens = x * 3 + y
                if cur_tokens < min_tokens:
                    min_tokens = cur_tokens
    if min_tokens != 401:
        answer1 += min_tokens
print("Answer 1:", answer1)

for line in input_list:
    line = line.splitlines()
    x1, y1 = [int(x[2:]) for x in line[0].split(": ")[1].split(", ")]
    x2, y2 = [int(x[2:]) for x in line[1].split(": ")[1].split(", ")]
    px, py = [int(x[2:]) + 10000000000000 for x in line[2].split(": ")[1].split(", ")]
    b = (py * x1 - px * y1) / (y2 * x1 - x2 * y1)
    a = (px - b * x2) / x1
    if int(a) * x1 + int(b) * x2 == px:
        answer2 += a * 3 + b
print("Answer 2:", int(answer2))
