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
            if (x, y, d) in visited:
                continue
            visited.add((x, y, d))
            match d:
                case "R":
                    if (x, y + 1) in maze:
                        energized.add((x, y + 1))
                        match maze[x, y + 1]:
                            case ".":  new_pos.append((x, y + 1, "R"))
                            case "/":  new_pos.append((x, y + 1, "U"))
                            case "\\": new_pos.append((x, y + 1, "D"))
                            case "-":  new_pos.append((x, y + 1, "R"))
                            case "|":
                                new_pos.append((x, y + 1, "U"))
                                new_pos.append((x, y + 1, "D"))
                case "L":
                    if (x, y - 1) in maze:
                        energized.add((x, y - 1))
                        match maze[x, y - 1]:
                            case ".":  new_pos.append((x, y - 1, "L"))
                            case "/":  new_pos.append((x, y - 1, "D"))
                            case "\\": new_pos.append((x, y - 1, "U"))
                            case "-":  new_pos.append((x, y - 1, "L"))
                            case "|":
                                new_pos.append((x, y - 1, "U"))
                                new_pos.append((x, y - 1, "D"))
                case "U":
                    if (x - 1, y) in maze:
                        energized.add((x - 1, y))
                        match maze[x - 1, y]:
                            case ".":  new_pos.append((x - 1, y, "U"))
                            case "/":  new_pos.append((x - 1, y, "R"))
                            case "\\": new_pos.append((x - 1, y, "L"))
                            case "-":
                                new_pos.append((x - 1, y, "L"))
                                new_pos.append((x - 1, y, "R"))
                            case "|":  new_pos.append((x - 1, y, "U"))
                case "D":
                    if (x + 1, y) in maze:
                        energized.add((x + 1, y))
                        match maze[x + 1, y]:
                            case ".":  new_pos.append((x + 1, y, "D"))
                            case "/":  new_pos.append((x + 1, y, "L"))
                            case "\\": new_pos.append((x + 1, y, "R"))
                            case "-":
                                new_pos.append((x + 1, y, "L"))
                                new_pos.append((x + 1, y, "R"))
                            case "|":  new_pos.append((x + 1, y, "D"))
        cur_pos = new_pos
    answer2.append(len(energized))
    if start_pos == (0, -1, "R"):
        print("Answer 1:", len(energized))
print("Answer 2:", max(answer2))
