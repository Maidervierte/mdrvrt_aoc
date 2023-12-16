""" 2023 aoc16 """

with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

maze = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        maze[i, j] = char

answer1 = []

start_posses = [(x, -1, "R") for x in range(len(input_list))] \
               + [(x, len(input_list[0]), "L") for x in range(len(input_list))] \
               + [(-1, x, "D") for x in range(len(input_list[0]))] \
               + [(len(input_list), x, "U") for x in range(len(input_list[0]))]
answer2 = []
for start_pos in start_posses:
    cur_pos = [start_pos]
    energized = set()
    visited = set()
    for _ in range(1000):
        new_pos = []
        for x, y, d in cur_pos:
            match d:
                case "R":
                    if (x, y + 1) in maze:
                        energized.add((x, y + 1))
                        match maze[x, y + 1]:
                            case ".":
                                new = (x, y + 1, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "/":
                                new = (x, y + 1, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "\\":
                                new = (x, y + 1, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "-":
                                new = (x, y + 1, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "|":
                                new = (x, y + 1, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                                new = (x, y + 1, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                case "L":
                    if (x, y - 1) in maze:
                        energized.add((x, y - 1))
                        match maze[x, y - 1]:
                            case ".":
                                new = (x, y - 1, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "/":
                                new = (x, y - 1, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "\\":
                                new = (x, y - 1, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "-":
                                new = (x, y - 1, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "|":
                                new = (x, y - 1, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                                new = (x, y - 1, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                case "U":
                    if (x - 1, y) in maze:
                        energized.add((x - 1, y))
                        match maze[x - 1, y]:
                            case ".":
                                new = (x - 1, y, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "/":
                                new = (x - 1, y, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "\\":
                                new = (x - 1, y, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "-":
                                new = (x - 1, y, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                                new = (x - 1, y, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "|":
                                new = (x - 1, y, "U")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                case "D":
                    if (x + 1, y) in maze:
                        energized.add((x + 1, y))
                        match maze[x + 1, y]:
                            case ".":
                                new = (x + 1, y, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "/":
                                new = (x + 1, y, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "\\":
                                new = (x + 1, y, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "-":
                                new = (x + 1, y, "L")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                                new = (x + 1, y, "R")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
                            case "|":
                                new = (x + 1, y, "D")
                                if new not in visited:
                                    new_pos.append(new)
                                    visited.add(new)
        cur_pos = new_pos
    answer2.append(len(energized))
    if start_pos == (0, -1, "R"):
        print("Answer 1:", len(energized))
print("Answer 2:", max(answer2))
