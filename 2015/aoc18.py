""" 2015 aoc18 """
with open("input18.txt", "r", encoding="utf-8") as f:
    grid = f.read().splitlines()

for i, line in enumerate(grid):
    grid[i] = list(line)

for _ in range(100):
    temp_grid = []
    for line in grid:
        temp_grid.append(line.copy())
    for x in range(len(grid)):
        for y in range(len(grid)):
            count = 0
            if x > 0 and y > 0 and grid[x - 1][y - 1] == "#": count += 1
            if x > 0 and grid[x - 1][y] == "#": count += 1
            if x > 0 and y < len(grid) - 1 and grid[x - 1][y + 1] == "#": count += 1

            if y > 0 and grid[x][y - 1] == "#": count += 1
            if y < len(grid) - 1 and grid[x][y + 1] == "#": count += 1

            if x < len(grid[0]) - 1 and y > 0 and grid[x + 1][y - 1] == "#": count += 1
            if x < len(grid[0]) - 1 and grid[x + 1][y] == "#": count += 1
            if x < len(grid[0]) - 1 and y < len(grid) - 1 and grid[x + 1][y + 1] == "#": count += 1
            if grid[x][y] == "#":
                if count < 2 or count > 3:
                    temp_grid[x][y] = "."
            if grid[x][y] == ".":
                if count == 3:
                    temp_grid[x][y] = "#"
    grid = []
    for line in temp_grid:
        grid.append(line.copy())

answer1 = 0
for x in range(len(grid)):
    for y in range(len(grid)):
        if grid[x][y] == "#":
            answer1 += 1

print("Answer 1:", answer1)

with open("input18.txt", "r", encoding="utf-8") as f:
    grid = f.read().splitlines()

for i, line in enumerate(grid):
    grid[i] = list(line)

grid[0][0] = "#"
grid[0][len(grid[0]) - 1] = "#"
grid[len(grid) - 1][0] = "#"
grid[len(grid) - 1][len(grid[0]) - 1] = "#"

for _ in range(100):
    temp_grid = []
    for line in grid:
        temp_grid.append(line.copy())
    for x in range(len(grid)):
        for y in range(len(grid)):
            if x == 0 and y == 0:
                continue
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                continue
            if x == 0 and y == len(grid[0]) - 1:
                continue
            if x == len(grid) - 1 and y == 0:
                continue
            count = 0
            if x > 0 and y > 0 and grid[x - 1][y - 1] == "#": count += 1
            if x > 0 and grid[x - 1][y] == "#": count += 1
            if x > 0 and y < len(grid) - 1 and grid[x - 1][y + 1] == "#": count += 1

            if y > 0 and grid[x][y - 1] == "#": count += 1
            if y < len(grid) - 1 and grid[x][y + 1] == "#": count += 1

            if x < len(grid[0]) - 1 and y > 0 and grid[x + 1][y - 1] == "#": count += 1
            if x < len(grid[0]) - 1 and grid[x + 1][y] == "#": count += 1
            if x < len(grid[0]) - 1 and y < len(grid) - 1 and grid[x + 1][y + 1] == "#": count += 1
            if grid[x][y] == "#":
                if count < 2 or count > 3:
                    temp_grid[x][y] = "."
            if grid[x][y] == ".":
                if count == 3:
                    temp_grid[x][y] = "#"
    grid = []
    for line in temp_grid:
        grid.append(line.copy())

answer2 = 0
for x in range(len(grid)):
    for y in range(len(grid)):
        if grid[x][y] == "#":
            answer2 += 1

print("Answer 2:", answer2)
