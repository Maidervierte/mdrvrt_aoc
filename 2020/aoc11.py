""" 2020 aoc11 """

with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

layout = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        layout[i, j] = char

for _ in range(200):
    temp = {}
    for key, value in layout.items():
        if value == "L":
            for seat in [(key[0] - 1, key[1]), (key[0] + 1, key[1]),
                         (key[0], key[1] - 1), (key[0], key[1] + 1),
                         (key[0] - 1, key[1] - 1), (key[0] - 1, key[1] + 1),
                         (key[0] + 1, key[1] - 1), (key[0] + 1, key[1] + 1)]:
                if seat in layout and layout[seat] == "#":
                    break
            else:
                temp[key] = "#"
                continue
            temp[key] = "L"
        if value == "#":
            occupied = 0
            for seat in [(key[0] - 1, key[1]), (key[0] + 1, key[1]),
                         (key[0], key[1] - 1), (key[0], key[1] + 1),
                         (key[0] - 1, key[1] - 1), (key[0] - 1, key[1] + 1),
                         (key[0] + 1, key[1] - 1), (key[0] + 1, key[1] + 1)]:
                if seat in layout and layout[seat] == "#":
                    occupied += 1
            if occupied >= 4:
                temp[key] = "L"
            else:
                temp[key] = "#"
    for key, value in temp.items():
        layout[key] = value
answer1 = list(layout.values()).count("#")
print("Answer 1:", answer1)

layout = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        layout[i, j] = char

for _ in range(200):
    temp = {}
    for key, value in layout.items():
        if value == "L":
            for seat in [(-1, 0), (1, 0),
                         (0, - 1), (0, + 1),
                         (- 1, - 1), (- 1, 1),
                         (1, - 1), (1, 1)]:
                visible_seat = (key[0] + seat[0], key[1] + seat[1])
                while visible_seat in layout and layout[visible_seat] == ".":
                    visible_seat = (visible_seat[0] + seat[0], visible_seat[1] + seat[1])
                if visible_seat in layout and layout[visible_seat] == "#":
                    break
            else:
                temp[key] = "#"
                continue
            temp[key] = "L"
        if value == "#":
            occupied = 0
            for seat in [(-1, 0), (1, 0),
                         (0, - 1), (0, + 1),
                         (- 1, - 1), (- 1, 1),
                         (1, - 1), (1, 1)]:
                visible_seat = (key[0] + seat[0], key[1] + seat[1])
                while visible_seat in layout and layout[visible_seat] == ".":
                    visible_seat = (visible_seat[0] + seat[0], visible_seat[1] + seat[1])
                if visible_seat in layout and layout[visible_seat] == "#":
                    occupied += 1
            if occupied >= 5:
                temp[key] = "L"
            else:
                temp[key] = "#"
    for key, value in temp.items():
        layout[key] = value
answer2 = list(layout.values()).count("#")
print("Answer 2:", answer2)
