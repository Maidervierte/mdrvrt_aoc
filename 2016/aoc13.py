""" 2016 aoc13 """

with open("input13.txt", "r", encoding="utf-8") as f:
    number = int(f.read())

goal = (31, 39)

visited = set()
visited.add((1, 1))


def wall(_x, _y):
    """check if location is a wall"""
    check_num = (_x * _x + 3 * _x + 2 * _x * _y + _y + _y * _y) + number
    bin_num = bin(check_num)
    if bin_num.count("1") % 2 == 0:
        return False
    return True


steps = 0
answer2 = 0
while goal not in visited:
    steps += 1
    print(steps)
    temp_visited = visited.copy()
    for x, y in visited:
        if x - 1 >= 0 and not wall(x - 1, y):
            temp_visited.add((x - 1, y))
        if not wall(x + 1, y):
            temp_visited.add((x + 1, y))
        if y - 1 >= 0 and not wall(x, y - 1):
            temp_visited.add((x, y - 1))
        if not wall(x, y + 1):
            temp_visited.add((x, y + 1))
    visited = temp_visited.copy()
    if steps == 50:
        answer2 = len(visited)

print("Answer 1:", steps)
print("Answer 2:", answer2)
