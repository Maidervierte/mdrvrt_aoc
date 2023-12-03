""" 2023 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

field = {}
around = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i, line in enumerate(input_list):
    for j, char in enumerate([*line]):
        field[(i, j)] = char

visited = set()
answer1 = 0
for (x, y) in field.keys():
    if (x, y) in visited or not field[(x, y)].isdigit():
        continue
    found = False
    number = [(x, y)]
    visited.add((x, y))
    if field[(x, y + 1)].isdigit():
        number.append((x, y + 1))
        visited.add((x, y + 1))
        if field[(x, y + 2)].isdigit():
            number.append((x, y + 2))
            visited.add((x, y + 2))
    for (x2, y2) in number:
        for a1, b1 in around:
            if not found and (x2 + a1, y2 + b1) in field \
                    and (not field[(x2 + a1, y2 + b1)].isdigit()) \
                    and field[x2 + a1, y2 + b1] != ".":
                answer1 += int("".join([field[(x3, y3)] for (x3, y3) in number]))
                found = True
                break

print("Answer 1:", answer1)

visited = set()


def check_around(a, b):
    """checks around a coord"""
    number2 = []
    (c, d) = (0, 0)
    for _a1, _b1 in around:
        if (a + _a1, b + _b1) not in visited and field[(a + _a1, b + _b1)].isdigit():
            (c, d) = (a + _a1, b + _b1)
            break
    if (c, d) == (0, 0):
        return 0
    number2.append((c, d))
    visited.add((c, d))
    if field[(c, d + 1)].isdigit():
        number2.append((c, d + 1))
        visited.add((c, d + 1))
        if field[(c, d + 2)].isdigit():
            number2.append((c, d + 2))
            visited.add((c, d + 2))
    if field[(c, d - 1)].isdigit():
        number2.insert(0, (c, d - 1))
        visited.add((c, d - 1))
        if field[(c, d - 2)].isdigit():
            number2.insert(0, (c, d - 2))
            visited.add((c, d - 2))
    return int("".join([field[(x3, y3)] for (x3, y3) in number2]))


answer2 = 0
for (x, y) in field.keys():
    if (x, y) in visited or not field[(x, y)].isdigit():
        continue
    found = False
    number = [(x, y)]
    visited.add((x, y))
    if field[(x, y + 1)].isdigit():
        number.append((x, y + 1))
        visited.add((x, y + 1))
        if field[(x, y + 2)].isdigit():
            number.append((x, y + 2))
            visited.add((x, y + 2))
    for (x2, y2) in number:
        for a1, b1 in around:
            if not found and (x2 + a1, y2 + b1) in field \
                    and (not field[(x2 + a1, y2 + b1)].isdigit()) \
                    and field[x2 + a1, y2 + b1] == "*":
                answer2 += int("".join([field[(x3, y3)] for (x3, y3) in number])) \
                           * check_around(x2 + a1, y2 + b1)
                found = True
                break

print("Answer 2:", answer2)
