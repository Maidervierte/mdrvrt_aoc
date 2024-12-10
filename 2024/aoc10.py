""" 2024 aoc10"""

with open("input10.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
heightmap = {}
trailheads = set()
trailscores = {}
trailratings = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == ".":
            continue
        heightmap[(i, j)] = int(char)
        if char == "0":
            trailheads.add((i, j))

for trailhead in trailheads:
    pos = set()
    visited = set()
    pos.add(trailhead)
    while pos:
        temp = set()
        for (i, j) in pos:
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (i + x, j + y) not in heightmap:
                    continue
                if heightmap[(i + x, j + y)] != (heightmap[i, j] + 1):
                    continue
                if heightmap[(i + x, j + y)] == 9 and (i + x, j + y) not in visited:
                    if trailhead in trailscores:
                        trailscores[trailhead] = trailscores[trailhead] + 1
                    else:
                        trailscores[trailhead] = 1
                visited.add((i + x, j + y))
                temp.add((i + x, j + y))
        pos = temp

    paths = [[trailhead]]
    while paths:
        new_paths = []
        for path in paths:
            (i, j) = path[-1]
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (i + x, j + y) not in visited:
                    continue
                if heightmap[(i + x, j + y)] != (heightmap[i, j] + 1):
                    continue
                temp = list(path)
                temp.append((i + x, j + y))
                new_paths.append(temp)
                if heightmap[(i + x, j + y)] != 9:
                    continue
                if trailhead in trailratings:
                    trailratings[trailhead] = trailratings[trailhead] + 1
                else:
                    trailratings[trailhead] = 1
        paths = new_paths
answer1 = sum(trailscores.values())
answer2 = sum(trailratings.values())
print("Answer 1:", answer1)
print("Answer 2:", answer2)
