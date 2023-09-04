""" 2016 aoc17 """
import hashlib

with open("input17.txt", "r", encoding="utf-8") as f:
    passcode = f.read()

_grid = "#########\n" \
        "#S| | | #\n" \
        "#-#-#-#-#\n" \
        "# | | | #\n" \
        "#-#-#-#-#\n" \
        "# | | | #\n" \
        "#-#-#-#-#\n" \
        "# | | |  \n" \
        "####### V".splitlines()

grid = []
for line in _grid:
    grid.append(list(line))

start_pos = (1, 1)
paths = set()
paths.add("")
visited = set()
visited.add(start_pos)
while (len(grid) - 2, len(grid[-2]) - 2) not in visited:
    temp_paths = set()
    for path in paths:
        x, y = start_pos
        for letter in path:
            match letter:
                case "U":
                    x -= 2
                case "D":
                    x += 2
                case "R":
                    y += 2
                case "L":
                    y -= 2
        pos_dir = []
        if grid[x - 1][y] == "-" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[0] in "bcdef":
            temp_paths.add(path + "U")
            visited.add((x - 2, y))
            if (len(grid) - 2, len(grid[-2]) - 2) in visited:
                print("Answer 1:", path + "U")
                break
        if grid[x + 1][y] == "-" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[1] in "bcdef":
            temp_paths.add(path + "D")
            visited.add((x + 2, y))
            if (len(grid) - 2, len(grid[-2]) - 2) in visited:
                print("Answer 1:", path + "D")
                break
        if grid[x][y + 1] == "|" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[3] in "bcdef":
            temp_paths.add(path + "R")
            visited.add((x, y + 2))
            if (len(grid) - 2, len(grid[-2]) - 2) in visited:
                print("Answer 1:", path + "R")
                break
        if grid[x][y - 1] == "|" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[2] in "bcdef":
            temp_paths.add(path + "L")
            visited.add((x, y - 2))
            if (len(grid) - 2, len(grid[-2]) - 2) in visited:
                print("Answer 1:", path + "L")
                break
    paths = set(temp_paths)

paths = set()
paths.add("")
visited = set()
visited.add(start_pos)
all_paths = set()
while len(paths) != 0:
    temp_paths = set()
    for path in paths:
        x, y = start_pos
        for letter in path:
            match letter:
                case "U":
                    x -= 2
                case "D":
                    x += 2
                case "R":
                    y += 2
                case "L":
                    y -= 2
        pos_dir = []
        if grid[x - 1][y] == "-" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[0] in "bcdef":
            if (x - 2, y) != (len(grid) - 2, len(grid[-2]) - 2):
                temp_paths.add(path + "U")
                visited.add((x - 2, y))
            else:
                all_paths.add(path + "U")
        if grid[x + 1][y] == "-" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[1] in "bcdef":
            if (x + 2, y) != (len(grid) - 2, len(grid[-2]) - 2):
                temp_paths.add(path + "D")
                visited.add((x + 2, y))
            else:
                all_paths.add(path + "D")
        if grid[x][y + 1] == "|" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[3] in "bcdef":
            if (x, y + 2) != (len(grid) - 2, len(grid[-2]) - 2):
                temp_paths.add(path + "R")
                visited.add((x, y + 2))
            else:
                all_paths.add(path + "R")
        if grid[x][y - 1] == "|" and \
                hashlib.md5((passcode + path).encode("utf-8")).hexdigest()[2] in "bcdef":
            if (x, y - 2) != (len(grid) - 2, len(grid[-2]) - 2):
                temp_paths.add(path + "L")
                visited.add((x, y - 2))
            else:
                all_paths.add(path + "L")
    paths = set(temp_paths)

max_len = 0
for path in all_paths:
    if len(path) > max_len:
        max_len = len(path)
print("Answer 2:", max_len)
