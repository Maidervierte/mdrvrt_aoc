""" 2015 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    number_list = f.read()

visited = set()
cur_pos = (0, 0)
visited.add(cur_pos)

for x in number_list:
    if x == "<":
        cur_pos = (cur_pos[0] - 1, cur_pos[1])
    if x == ">":
        cur_pos = (cur_pos[0] + 1, cur_pos[1])
    if x == "v":
        cur_pos = (cur_pos[0], cur_pos[1] - 1)
    if x == "^":
        cur_pos = (cur_pos[0], cur_pos[1] + 1)
    visited.add(cur_pos)
visited2 = set()
cur_pos_santa = (0, 0)
cur_pos_robo = (0, 0)
visited2.add(cur_pos_santa)
santa = True
for x in number_list:
    if santa:
        if x == "<":
            cur_pos_santa = (cur_pos_santa[0] - 1, cur_pos_santa[1])
        if x == ">":
            cur_pos_santa = (cur_pos_santa[0] + 1, cur_pos_santa[1])
        if x == "v":
            cur_pos_santa = (cur_pos_santa[0], cur_pos_santa[1] - 1)
        if x == "^":
            cur_pos_santa = (cur_pos_santa[0], cur_pos_santa[1] + 1)
        visited2.add(cur_pos_santa)
        santa = False
    else:
        if x == "<":
            cur_pos_robo = (cur_pos_robo[0] - 1, cur_pos_robo[1])
        if x == ">":
            cur_pos_robo = (cur_pos_robo[0] + 1, cur_pos_robo[1])
        if x == "v":
            cur_pos_robo = (cur_pos_robo[0], cur_pos_robo[1] - 1)
        if x == "^":
            cur_pos_robo = (cur_pos_robo[0], cur_pos_robo[1] + 1)
        visited2.add(cur_pos_robo)
        santa = True

print("Answer 1:", len(visited))
print("Answer 2:", len(visited2))
