""" 2023 aoc17 """
import heapq

with open("input17.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

block = {}
for i, line in enumerate(input_list):
    # print(line)
    for j, char in enumerate(line):
        block[i, j] = int(char)


def solve(part, a, b):
    """solve"""
    start = (0, 0, (0, 0), "")
    queue = [start]
    visited = set()
    end = ((len(input_list) - 1), len(input_list[0]) - 1)
    while queue:
        cur_pos = heapq.heappop(queue)
        (x, y) = cur_pos[2]
        (_x, _y) = (x, y)
        old_direction = cur_pos[3]
        if (x, y, old_direction) in visited:
            continue
        visited.add((x, y, old_direction))
        # print(cur_pos)
        if (x, y) == end:
            print("Answer " + part + ":", cur_pos[0])
            break
        for pos_add in range(a, b):
            (x, y) = cur_pos[2]
            for ((x, y), direction) in [((x + pos_add, y), "D"), ((x - pos_add, y), "U"), ((x, y + pos_add), "R"),
                                        ((x, y - pos_add), "L")]:
                if (x, y) not in block:
                    continue
                if (old_direction, direction) in [("D", "D"), ("U", "U"), ("R", "R"), ("L", "L"),
                                                  ("U", "D"), ("U", "D"), ("L", "R"), ("R", "L")]:
                    continue
                if (x, y, direction) in visited:
                    continue
                new_distance = cur_pos[0]
                if x == _x:
                    if y < _y:
                        for i in range(y, _y):
                            new_distance += block[x, i]
                    else:
                        for i in range(_y + 1, y + 1):
                            new_distance += block[x, i]
                else:
                    if x < _x:
                        for i in range(x, _x):
                            new_distance += block[i, y]
                    else:
                        for i in range(_x + 1, x + 1):
                            new_distance += block[i, y]
                heuristic = 0
                heapq.heappush(queue, (new_distance, heuristic, (x, y), direction))


solve("1", 1, 4)
solve("2", 4, 11)
