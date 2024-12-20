""" 2024 aoc20"""

with open("input20.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

base = 0
start = (0, 0)
end = (0, 0)
grid = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        grid[i, j] = char
        if char == "S":
            grid[i, j] = "."
            start = (i, j)
        if char == "E":
            grid[i, j] = "."
            end = (i, j)

time_from_start = {}
paths = [start]
time_from_start[start] = 0
visited = set()
visited.add(start)
for picoseconds in range(len(grid)):
    temp_paths = []
    for (x, y) in paths:
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + i, y + j) not in grid:
                continue
            if grid[(x + i, y + j)] == "#":
                continue
            if (x + i, y + j) in visited:
                continue
            temp_paths.append((x + i, y + j))
            visited.add((x + i, y + j))
            time_from_start[(x + i, y + j)] = picoseconds + 1
    paths = temp_paths
    if not paths:
        break

base_time = time_from_start[end]
time_from_end = {}
for key, value in time_from_start.items():
    time_from_end[key] = base_time - value

cheats1 = {}
max_dist1 = 2
cheats2 = {}
max_dist2 = 20
for (x1, y1), t1 in time_from_start.items():
    for (x2, y2), t2 in time_from_end.items():
        distance = abs(x1 - x2) + abs(y1 - y2)
        if distance > max_dist2:
            continue
        time_with_cheat = t1 + t2 + distance
        if time_with_cheat < base_time:
            if base_time - time_with_cheat in cheats2:
                cheats2[base_time - time_with_cheat] += 1
            else:
                cheats2[base_time - time_with_cheat] = 1
            if distance > max_dist1:
                continue
            if base_time - time_with_cheat in cheats1:
                cheats1[base_time - time_with_cheat] += 1
            else:
                cheats1[base_time - time_with_cheat] = 1

# print(sorted(cheats1.items()))
# print([(x, y) for (x, y) in sorted(cheats2.items()) if x >= 50])
answer1 = sum(y if x >= 100 else 0 for (x, y) in cheats1.items())
answer2 = sum(y if x >= 100 else 0 for (x, y) in cheats2.items())
print("Answer 1:", answer1)
print("Answer 2:", answer2)
