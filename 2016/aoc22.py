""" 2016 aoc22 """
with open("input22.txt", "r", encoding="utf-8") as f:
    nodes_list = f.read().splitlines()

# nodes_list = "root@ebhq-gridcenter# df -h\n" \
#              "Filesystem            Size  Used  Avail  Use%\n" \
#              "/dev/grid/node-x0-y0   10T    8T     2T   80%\n" \
#              "/dev/grid/node-x0-y1   11T    6T     5T   54%\n" \
#              "/dev/grid/node-x0-y2   32T   28T     4T   87%\n" \
#              "/dev/grid/node-x1-y0    9T    7T     2T   77%\n" \
#              "/dev/grid/node-x1-y1    8T    0T     8T    0%\n" \
#              "/dev/grid/node-x1-y2   11T    7T     4T   63%\n" \
#              "/dev/grid/node-x2-y0   10T    6T     4T   60%\n" \
#              "/dev/grid/node-x2-y1    9T    8T     1T   88%\n" \
#              "/dev/grid/node-x2-y2    9T    6T     3T   66%".splitlines()
nodes = {}
max_x = 0
max_y = 0
for node in nodes_list[2:]:
    node_split = list(filter(None, node.split(" ")))
    x = int(node_split[0].split("-")[1][1:])
    y = int(node_split[0].split("-")[2][1:])
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    s = int(node_split[1][:-1])
    u = int(node_split[2][:-1])
    a = int(node_split[3][:-1])
    nodes[(x, y)] = (s, u, a)

viable = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        for _x in range(max_x + 1):
            for _y in range(max_y + 1):
                if (x, y) != (_x, _y) and nodes[(x, y)][1] <= nodes[(_x, _y)][2] and nodes[(x, y)][1] != 0:
                    viable += 1
print("Answer 1:", viable)

goal = (0, 0)
data = (max_x, 0)
for ((x, y), (_, u, _)) in nodes.items():
    if u == 0:
        hole = (x, y)

maze = [["." for y in range(max_y + 1)] for x in range(max_x + 1)]

for ((x, y), (s, u, _)) in nodes.items():
    if u == 0:
        hole = (x, y)
    if s > 99:
        maze[x][y] = "#"

# for __x in range(max_x + 1):
#     for __y in range(max_y + 1):
#         __s, __u, __a = nodes[__x, __y]
#         if (__x, __y) == data:
#             print("[", end="")
#         print(__u, "/", __s, end="")
#         if (__x, __y) == data:
#             print("]", end="")
#         print(end=" - ")
#     print()
# print()

visited = set()
visited.add(hole)
steps = 0
while (data[0] - 1, data[1]) not in visited:
    temp = set()
    for (x, y) in visited:
        if x < max_x:
            if maze[x + 1][y] != "#":
                temp.add((x + 1, y))
        if x > 0:
            if maze[x - 1][y] != "#":
                temp.add((x - 1, y))
        if y < max_y:
            if maze[x][y + 1] != "#":
                temp.add((x, y + 1))
        if y > 0:
            if maze[x][y - 1] != "#":
                temp.add((x, y - 1))
    steps += 1
    visited = temp.copy()

visited = set()
visited.add(data)
_steps = 0
while (0,0) not in visited:
    temp = set()
    for (x, y) in visited:
        if x < max_x:
            if maze[x + 1][y] != "#":
                temp.add((x + 1, y))
        if x > 0:
            if maze[x - 1][y] != "#":
                temp.add((x - 1, y))
        if y < max_y:
            if maze[x][y + 1] != "#":
                temp.add((x, y + 1))
        if y > 0:
            if maze[x][y - 1] != "#":
                temp.add((x, y - 1))
    _steps += 1
    visited = temp.copy()

print("Answer 2:", steps + (_steps - 1) * 5 + 1)

# cur_node = (max_x, 0)
# nodes[(-1, -1)] = (max_x, 0, 0)
# states = set()
# states.add(frozenset(nodes.items()))
# new_states = states.copy()
# all_states = states.copy()
# stop = False
# step = 0
# for __x in range(max_x + 1):
#     for __y in range(max_y + 1):
#         __s, __u, __a = nodes[__x, __y]
#         if (__x, __y) == cur_node:
#             print("[", end="")
#         print(__u, "/", __s, end="")
#         if (__x, __y) == cur_node:
#             print("]", end="")
#         print(end=" - ")
#     print()
# print()
# while not stop:
#     print("#################################")
#     print(str(step) + ":", len(new_states),"/",len(all_states))
#     states = new_states.copy()
#     new_states = set()
#     for state in states:
#         cur_nodes = dict(state)
#         (_x, _y, _) = cur_nodes[(-1, -1)]
#         # for __x in range(max_x + 1):
#         #     for __y in range(max_y + 1):
#         #         __s, __u, __a = cur_nodes[__x, __y]
#         #         if (__x, __y) == (_x, _y):
#         #             print("[", end="")
#         #         print(__u, "/", __s, end="")
#         #         if (__x, __y) == (_x, _y):
#         #             print("]", end="")
#         #         print(end=" - ")
#         #     print()
#         # print()
#         if (_x, _y) == (0, 0):
#             stop = True
#             break
#         for ((x, y), (s, u, a)) in state:
#             if u==0 or x==-1:
#                 continue
#             # print("this node:",x,y,"|",u,"/",s)
#             if x > 0:
#                 temp_nodes = cur_nodes.copy()
#                 _s, _u, _a = temp_nodes[(x - 1, y)]
#                 # print("  1:",_u,"/",_s)
#                 if u <= _a:
#                     # print("yes")
#                     temp_nodes[(x, y)] = (s, 0, s)
#                     temp_nodes[(x - 1, y)] = (_s, _u + u, _a - u)
#                     if (x, y) == (_x, _y):
#                         temp_nodes[(-1, -1)] = (x - 1, y, 0)
#                     new_state = frozenset(temp_nodes.items())
#                     if new_state not in all_states:
#                         new_states.add(new_state)
#                         all_states.add(new_state)
#             if x < max_x:
#                 temp_nodes = cur_nodes.copy()
#                 _s, _u, _a = temp_nodes[(x + 1, y)]
#                 # print("  2:",_u,"/",_s)
#                 if u <= _a:
#                     # print("yes")
#                     temp_nodes[(x, y)] = (s, 0, s)
#                     temp_nodes[(x + 1, y)] = (_s, _u + u, _a - u)
#                     if (x, y) == (_x, _y):
#                         temp_nodes[(-1, -1)] = (x + 1, y, 0)
#                     new_state = frozenset(temp_nodes.items())
#                     if new_state not in all_states:
#                         new_states.add(new_state)
#                         all_states.add(new_state)
#             if y > 0:
#                 temp_nodes = cur_nodes.copy()
#                 _s, _u, _a = temp_nodes[(x, y - 1)]
#                 # print("  3:",_u,"/",_s)
#                 if u <= _a:
#                     # print("yes")
#                     temp_nodes[(x, y)] = (s, 0, s)
#                     temp_nodes[(x, y - 1)] = (_s, _u + u, _a - u)
#                     if (x, y) == (_x, _y):
#                         temp_nodes[(-1, -1)] = (x, y - 1, 0)
#                     new_state = frozenset(temp_nodes.items())
#                     if new_state not in all_states:
#                         new_states.add(new_state)
#                         all_states.add(new_state)
#             if y < max_y:
#                 temp_nodes = cur_nodes.copy()
#                 _s, _u, _a = temp_nodes[(x, y + 1)]
#                 # print("  4:",_u,"/",_s)
#                 if u <= _a:
#                     # print("yes")
#                     temp_nodes[(x, y)] = (s, 0, s)
#                     temp_nodes[(x, y + 1)] = (_s, _u + u, _a - u)
#                     if (x, y) == (_x, _y):
#                         temp_nodes[(-1, -1)] = (x, y + 1, 0)
#                     new_state = frozenset(temp_nodes.items())
#                     if new_state not in all_states:
#                         new_states.add(new_state)
#                         all_states.add(new_state)
#     step += 1
