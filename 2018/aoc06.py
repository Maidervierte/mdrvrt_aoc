""" 2018 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = [(int(x.split(", ")[0]), int(x.split(", ")[1])) for x in f.read().splitlines()]

max_x = 0
max_y = 0
mult = 2
for (x, y) in input_list:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

grid = {}
closest_pair = (0, 0)
for x in range(-max_x * mult, max_x * mult + 1):
    for y in range(-max_y * mult, max_y * mult + 1):
        shortest = max_x * max_y
        for (_x, _y) in input_list:
            cur_dist = abs(x - _x) + abs(y - _y)
            if cur_dist == shortest:
                closest_pair = (-max_x * mult, max_y * mult + 1)
            if cur_dist < shortest:
                shortest = cur_dist
                closest_pair = (_x, _y)
        grid[(x, y)] = closest_pair

valid_pairs = input_list.copy()
for x in range(-max_x * mult, max_x * mult):
    if grid[(x, -max_y * mult)] in valid_pairs:
        valid_pairs.remove(grid[(x, -max_y * mult)])
    if grid[(x, max_y * mult)] in valid_pairs:
        valid_pairs.remove(grid[(x, max_y * mult)])
for y in range(-max_y * mult, max_y * mult):
    if grid[(-max_x * mult, y)] in valid_pairs:
        valid_pairs.remove(grid[(-max_x * mult, y)])
    if grid[(max_x * mult, y)] in valid_pairs:
        valid_pairs.remove(grid[(max_x * mult, y)])

pairs = {}
for (_, _), (x, y) in grid.items():
    if (x, y) in valid_pairs:
        if (x, y) in pairs:
            pairs[(x, y)] += 1
        else:
            pairs[(x, y)] = 1

max_v = 0
for key, value in pairs.items():
    max_v = max(max_v, value)
print("Answer 1:", max_v)

answer2 = 0
for x in range(-max_x - 10000, max_x + 10000):
    for y in range(-max_y - 10000, max_y + 10000):
        if abs(x) + abs(y) > 10000 + max_x + max_y:
            continue
        total_dist = 0
        too_far = False
        for _x, _y in input_list:
            total_dist += abs(x - _x) + abs(y - _y)
            if total_dist >= 10000:
                too_far = True
                break
        if not too_far:
            answer2 += 1
print("Answer 2:", answer2)
