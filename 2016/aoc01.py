""" 2016 aoc01 """
with open("input01.txt", "r", encoding="utf-8") as f:
    number_list = f.read().split(", ")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def add(x, y):
    return (x[0] + y[0], y[1] + x[1])


dest_pos = (0, 0)
cur_dir = 0
visited = set()
visited.add((0, 0))
found = True
for x in number_list:
    if x[0] == "L":
        cur_dir -= 1
    if x[0] == "R":
        cur_dir += 1
    if cur_dir == -1: cur_dir = 3
    if cur_dir == 4: cur_dir = 0
    for y in range(int(x[1:].strip())):
        dest_pos = add(dest_pos, directions[cur_dir])
        if dest_pos in visited and found:
            dist2 = abs(dest_pos[0]) + abs(dest_pos[1])
            found = False
        visited.add(dest_pos)

dist = abs(dest_pos[0]) + abs(dest_pos[1])
print("Answer 1:", dist)
print("Answer 2:", dist2)
