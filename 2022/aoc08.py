""" 2022 aoc08 """
with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def vis_top(_input_list, position):
    """vis_top"""
    for _i1, _line in enumerate(_input_list):
        if _i1 >= position[0]:
            continue
        for _i2, _tree in enumerate(_line):
            if _i2 != position[1]:
                continue
            if int(_tree) >= int(_input_list[position[0]][position[1]]):
                return False
    return True


def vis_down(_input_list, position):
    """vis_down"""
    for _i1, _line in enumerate(_input_list):
        if _i1 <= position[0]:
            continue
        for _i2, _tree in enumerate(_line):
            if _i2 != position[1]:
                continue
            if int(_tree) >= int(_input_list[position[0]][position[1]]):
                return False
    return True


def vis_left(_input_list, position):
    """vis_left"""
    for _i1, _line in enumerate(_input_list):
        if _i1 != position[0]:
            continue
        for _i2, _tree in enumerate(_line):
            if _i2 >= position[1]:
                continue
            if int(_tree) >= int(_input_list[position[0]][position[1]]):
                return False
    return True


def vis_right(_input_list, position):
    """vis_right"""
    for _i1, _line in enumerate(_input_list):
        if _i1 != position[0]:
            continue
        for i2, tree in enumerate(_line):
            if i2 <= position[1]:
                continue
            if int(tree) >= int(_input_list[position[0]][position[1]]):
                return False
    return True


visible = 0
max_visible = 0
for i1, line in enumerate(input_list):
    for i2, tree in enumerate(line):
        if i1 == 0 or i2 == 0 or i1 == len(input_list) - 1 or i2 == len(line) - 1:
            visible += 1
            continue
        temp = 1
        if vis_top(input_list, (i1, i2)) \
                or vis_down(input_list, (i1, i2)) \
                or vis_left(input_list, (i1, i2)) \
                or vis_right(input_list, (i1, i2)):
            visible += 1
        for directions in [[i1 - 1, -1, -1, False],
                           [i1 + 1, len(input_list), 1, False],
                           [i2 - 1, -1, -1, True],
                           [i2 + 1, len(line), 1, True]]:
            counter, y, breaks = 0, i2, True
            for x in range(directions[0], directions[1], directions[2]):
                if breaks and directions[3]:
                    y, x = x, i1
                if breaks and int(input_list[x][y]) < int(tree):
                    counter += 1
                elif breaks:
                    counter, breaks = counter + 1, False
            temp *= counter
        max_visible = max(max_visible, temp)

print("Answer 1:", visible)
print("Answer 2:", max_visible)
