""" 2024 aoc18"""

with open("input18.txt", "r", encoding="utf-8") as f:
    input_list = [[int(y) for y in x.split(",")] for x in f.read().splitlines()]

answer1 = 0
answer2 = 0
grid = {}
vert = 70
hori = 70
simcount = 1024
for x in range(vert + 1):
    for y in range(hori + 1):
        grid[x, y] = "."

for i, line in enumerate(input_list):
    if i == simcount:
        break
    y, x = line
    grid[x, y] = "#"
end = (hori, vert)

for s, (s1, s2) in enumerate(input_list[simcount:]):
    grid[(s2, s1)] = "#"
    visited = set()
    paths = [(0, 0)]
    for step in range(1, vert * hori + 10):
        temp_paths = []
        for (x, y) in sorted(paths):
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + i, y + j) not in grid:
                    continue
                if grid[(x + i, y + j)] == "#":
                    continue
                if (x + i, y + j) in visited:
                    continue
                visited.add((x + i, y + j))
                temp_paths.append((x + i, y + j))
                if (x + i, y + j) == end:
                    if answer1 == 0:
                        answer1 = step
                    break
            else:
                continue
            break
        else:
            paths = temp_paths
            if not paths:
                answer2 = str(s1) + "," + str(s2)
                break
            continue
        break
    if answer2 != 0:
        break

print("Answer 1:", answer1)
print("Answer 2:", answer2)
