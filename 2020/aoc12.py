""" 2020 aoc12 """

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = [[x[0], int(x[1:])] for x in f.read().splitlines()]


def cardinal(direction, distance, position):
    """cardinal"""
    new_pos = position
    match direction:
        case "N":
            new_pos = (position[0] + distance, position[1])
        case "E":
            new_pos = (position[0], position[1] + distance)
        case "S":
            new_pos = (position[0] - distance, position[1])
        case "W":
            new_pos = (position[0], position[1] - distance)
    return new_pos


cur_dir = "E"
cur_pos = (0, 0)
cardinals = ["N", "E", "S", "W"]
for new_dir, dis in input_list:
    if new_dir in ["N", "E", "S", "W"]:
        cur_pos = cardinal(new_dir, dis, cur_pos)
    match new_dir:
        case "L":
            cur_dir = cardinals[cardinals.index(cur_dir) - (dis // 90)]
        case "R":
            cur_dir = cardinals[(cardinals.index(cur_dir) + (dis // 90)) % 4]
        case "F":
            cur_pos = cardinal(cur_dir, dis, cur_pos)
answer1 = sum([abs(cur_pos[0]), abs(cur_pos[1])])
print("Answer 1:", answer1)

cur_dir = "E"
cur_pos = (0, 0)
way_pos = (1, 10)
cardinals = ["N", "E", "S", "W"]
for new_dir, dis in input_list:
    if new_dir in ["N", "E", "S", "W"]:
        way_pos = cardinal(new_dir, dis, way_pos)
    match new_dir:
        case "L":
            cur_dir = cardinals[cardinals.index(cur_dir) - (dis // 90)]
        case "R":
            cur_dir = cardinals[(cardinals.index(cur_dir) + (dis // 90)) % 4]
        # case "F":
        #     cur_pos = cardinal(cur_dir, dis, cur_pos)
answer2 = sum([abs(cur_pos[0]), abs(cur_pos[1])])
print("Answer 2:", answer2)
