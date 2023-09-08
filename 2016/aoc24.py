""" 2016 aoc24 """
from itertools import permutations

with open("input24.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

max_num = 0
maze = {}
for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char.isdigit():
            max_num = max(int(char), max_num)
        maze[(i, j)] = char

fastest = {}
for i in range(max_num + 1):
    for j in range(i + 1, max_num + 1):
        _from = [_ for _ in maze if maze[_] == str(i)][0]
        _to = [_ for _ in maze if maze[_] == str(j)][0]
        # print(i, _from, "->", j, _to)
        visited = set()
        visited.add(_from)
        steps = 0
        while _to not in visited:
            _visited = set()
            for x, y in visited:
                if (x - 1, y) in maze and maze[(x - 1, y)] != "#":
                    _visited.add((x - 1, y))
                if (x + 1, y) in maze and maze[(x + 1, y)] != "#":
                    _visited.add((x + 1, y))
                if (x, y - 1) in maze and maze[(x, y - 1)] != "#":
                    _visited.add((x, y - 1))
                if (x, y + 1) in maze and maze[(x, y + 1)] != "#":
                    _visited.add((x, y + 1))
            visited = _visited
            steps += 1
        fastest[(i, j)] = steps
        fastest[(j, i)] = steps

to_visit = list(range(1,8))
min_dist = sum(fastest.values())
for perm in permutations(to_visit):
    cur_dist = 0
    prev = 0
    for cur in perm:
        cur_dist += fastest[(prev, cur)]
        prev = cur
        if cur_dist > min_dist:
            break
    min_dist = min(min_dist, cur_dist)

print("Answer 1:", min_dist)

min_dist = sum(fastest.values())
for perm in permutations(to_visit):
    cur_dist = 0
    prev = 0
    for cur in perm:
        cur_dist += fastest[(prev, cur)]
        prev = cur
        if cur_dist > min_dist:
            break
    cur_dist += fastest[(cur, 0)]
    min_dist = min(min_dist, cur_dist)

print("Answer 2:", min_dist)
