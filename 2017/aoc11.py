""" 2017 aoc11 """

with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split(",")


def get_distance(move_list):
    """calculates... the distance"""
    x = 0
    y = 0
    for move in move_list:
        match move:
            case "n":
                x += 1
            case "ne":
                x += 1
                y -= 1
            case "nw":
                y += 1
            case "s":
                x -= 1
            case "se":
                y -= 1
            case "sw":
                x -= 1
                y += 1
    if x >= 0 and y >= 0:
        return x + y
    if x <= 0 and y <= 0:
        return abs(x + y)
    return max(abs(x), abs(y))


print("Answer 1:", get_distance(input_list))

max_dist = 0
sub_list = []
for step in input_list:
    sub_list.append(step)
    max_dist = max(max_dist, get_distance(sub_list))

print("Answer 2:", max_dist)
