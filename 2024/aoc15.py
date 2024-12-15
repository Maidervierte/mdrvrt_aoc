""" 2024 aoc15"""

with open("input15.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0


def canMove(pos, _dir):
    """canMove"""
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == ".":
        return True
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == "#":
        return False
    return canMove((pos[0] + _dir[0], pos[1] + _dir[1]), _dir)


def toMove(pos, _dir):
    """toMove"""
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1])) != ".":
        toMove((pos[0] + _dir[0], pos[1] + _dir[1]), _dir)
    warehouse[(pos[0] + _dir[0], pos[1] + _dir[1])] = warehouse.get(pos)
    warehouse[pos] = "."


def canMove2(pos, _dir):
    """canMove2"""
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == ".":
        return True
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == "#":
        return False
    if _dir[0] == 0 \
            and (warehouse.get((pos[0], pos[1] + _dir[1]), "#") == "["
                 or warehouse.get((pos[0], pos[1] + _dir[1]), "#") == "]"):
        return canMove2((pos[0], pos[1] + _dir[1]), _dir)
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == "[":
        return canMove2((pos[0] + _dir[0], pos[1] + _dir[1]), _dir) and \
            canMove2((pos[0] + _dir[0], pos[1] + _dir[1] + 1), _dir)
    if warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1]), "#") == "]":
        return canMove2((pos[0] + _dir[0], pos[1] + _dir[1] * 3), _dir) and \
            canMove2((pos[0] + _dir[0], pos[1] + _dir[1] - 1), _dir)
    return False


def toMove2(pos, _dir):
    """toMove2"""
    if _dir[0] == 0 and \
            (warehouse.get((pos[0], pos[1] + _dir[1])) == "["
             or warehouse.get((pos[0], pos[1] + _dir[1])) == "]"):
        toMove2((pos[0], pos[1] + _dir[1]), _dir)
    if _dir[0] != 0 and warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1])) == "[":
        toMove2((pos[0] + _dir[0], pos[1] + _dir[1]), _dir)
        toMove2((pos[0] + _dir[0], pos[1] + _dir[1] + 1), _dir)
    if _dir[0] != 0 and warehouse.get((pos[0] + _dir[0], pos[1] + _dir[1])) == "]":
        toMove2((pos[0] + _dir[0], pos[1] + _dir[1]), _dir)
        toMove2((pos[0] + _dir[0], pos[1] + _dir[1] - 1), _dir)
    warehouse[(pos[0] + _dir[0], pos[1] + _dir[1])] = warehouse.get(pos)
    warehouse[pos] = "."


i = 0
robot = (0, 0)
warehouse = {}
for i, line in enumerate(input_list):
    if line == "":
        break
    for j, char in enumerate(line):
        warehouse[(i, j)] = char
        if char == "@":
            robot = (i, j)

moves = list("".join(input_list[i + 1:]))
input_robot = tuple(robot)
input_warehouse = dict(warehouse)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arrows = ["^", "v", "<", ">"]
for move in moves:
    move_dir = dirs[arrows.index(move)]
    if canMove(robot, move_dir):
        toMove(robot, move_dir)
        robot = (robot[0] + move_dir[0], robot[1] + move_dir[1])

for key, value in warehouse.items():
    if value == "O":
        answer1 += 100 * key[0] + key[1]
print("Answer 1:", answer1)

robot = (0, 0)
warehouse = {}
for i, line in enumerate(input_list):
    if line == "":
        break
    for j, char in enumerate(line):
        if char == "#":
            warehouse[(i, j * 2)] = "#"
            warehouse[(i, j * 2 + 1)] = "#"
        if char == ".":
            warehouse[(i, j * 2)] = "."
            warehouse[(i, j * 2 + 1)] = "."
        if char == "O":
            warehouse[(i, j * 2)] = "["
            warehouse[(i, j * 2 + 1)] = "]"
        if char == "@":
            robot = (i, j * 2)
            warehouse[(i, j * 2)] = "@"
            warehouse[(i, j * 2 + 1)] = "."

for i, move in enumerate(moves):
    move_dir = dirs[arrows.index(move)]
    if canMove2(robot, move_dir):
        toMove2(robot, move_dir)
        robot = (robot[0] + move_dir[0], robot[1] + move_dir[1])

for key, value in warehouse.items():
    if value == "[":
        answer2 += 100 * key[0] + key[1]
print("Answer 2:", answer2)
