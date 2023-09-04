""" 2016 aoc18 """
with open("input18.txt", "r", encoding="utf-8") as f:
    start = f.read()
room = [start]
for i in range(39):
    next_floor = ""
    for j, tile in enumerate(room[i]):
        prev = ""
        if j > 0:
            prev += room[i][j - 1]
        else:
            prev += "."
        prev += tile
        if j < (len(room[i]) - 1):
            prev += room[i][j + 1]
        else:
            prev += "."
        match prev:
            case "^^.":
                next_floor += "^"
            case ".^^":
                next_floor += "^"
            case "^..":
                next_floor += "^"
            case "..^":
                next_floor += "^"
            case _:
                next_floor += "."
    room.append(next_floor)

answer1 = 0
for floor in room:
    answer1 += floor.count(".")
print("Answer 1:", answer1)

room = [start]
for i in range(399999):
    next_floor = ""
    for j, tile in enumerate(room[i]):
        prev = ""
        if j > 0:
            prev += room[i][j - 1]
        else:
            prev += "."
        prev += tile
        if j < (len(room[i]) - 1):
            prev += room[i][j + 1]
        else:
            prev += "."
        match prev:
            case "^^.":
                next_floor += "^"
            case ".^^":
                next_floor += "^"
            case "^..":
                next_floor += "^"
            case "..^":
                next_floor += "^"
            case _:
                next_floor += "."
    room.append(next_floor)

answer2 = 0
for floor in room:
    answer2 += floor.count(".")
print("Answer 2:", answer2)
