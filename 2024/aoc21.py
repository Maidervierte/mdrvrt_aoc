""" 2024 aoc21"""

with open("input21.txt", "r", encoding="utf-8") as f:
    input_list = [list(x) for x in f.read().splitlines()]

answer1 = 0
answer2 = 0
keypad1 = {(0, 0): "7", (0, 1): "8", (0, 2): "9",
           (1, 0): "4", (1, 1): "5", (1, 2): "6",
           (2, 0): "1", (2, 1): "2", (2, 2): "3",
           (3, 1): "0", (3, 2): "A"}

keypad2 = {(0, 1): "^", (0, 2): "A",
           (1, 0): "<", (1, 1): "v", (1, 2): ">"}

start1 = (3, 2)
robot1 = []
for i, code in enumerate(input_list):
    code_path = []
    for char in code:
        char_code = []
        if keypad1[start1] == char:
            code_path.append(["A"])
            continue
        paths = [[[], [start1]]]
        while True:
            temp_paths = []
            for path in paths:
                (x, y) = path[1][-1]
                for i, j, c in [(1, 0, "v"), (-1, 0, "^"), (0, -1, "<"), (0, 1, ">")]:
                    if (x + i, y + j) in keypad1:
                        temp_path = list(path[1])
                        temp_code = list(path[0])
                        temp_path.append((x + i, y + j))
                        temp_code.append(c)
                        if keypad1[(x + i, y + j)] == char:
                            temp_code.append("A")
                            char_code.append("".join(temp_code))
                            start1 = (x + i, y + j)
                        temp_paths.append([list(temp_code), list(temp_path)])
            else:
                paths = temp_paths
                if char_code:
                    code_path.append(char_code)
                    break
                continue
    robot1.append(code_path)

combs = []
for robot in robot1:
    prev = list(robot[0])
    for i in range(1, len(robot)):
        t1 = []
        for j in robot[i]:
            for t2 in prev:
                t1.append("".join(t2) + j)
        prev = t1
    combs.append(prev)
robot1 = combs

start2 = (0, 2)
robot2 = []
for i, codes in enumerate(robot1):
    codes_path = []
    for code in codes:
        code_path = []
        for char in code:
            char_code = []
            if keypad2[start2] == char:
                code_path.append(["A"])
                continue
            paths = [[[], [start2]]]
            while True:
                temp_paths = []
                for path in paths:
                    (x, y) = path[1][-1]
                    for i, j, c in [(1, 0, "v"), (-1, 0, "^"), (0, -1, "<"), (0, 1, ">")]:
                        if (x + i, y + j) in keypad2:
                            temp_path = list(path[1])
                            temp_code = list(path[0])
                            temp_path.append((x + i, y + j))
                            temp_code.append(c)
                            if keypad2[(x + i, y + j)] == char:
                                temp_code.append("A")
                                char_code.append("".join(temp_code))
                                start2 = (x + i, y + j)
                            temp_paths.append([list(temp_code), list(temp_path)])
                else:
                    paths = temp_paths
                    if char_code:
                        code_path.append(char_code)
                        break
                    continue
        codes_path.append(code_path)
    robot2.append(codes_path)

combs_outer = []
for robot in robot2:
    combs = []
    for code in robot:
        prev = list(code[0])
        for i in range(1, len(code)):
            t1 = []
            for j in code[i]:
                for t2 in prev:
                    t1.append("".join(t2) + j)
            prev = t1
        combs.append(prev)
    combs_outer.append(combs)
robot2 = combs_outer

start2 = (0, 2)
robot3 = []
for i, outer_codes in enumerate(robot2):
    outer_codes_path = []
    for codes in outer_codes:
        codes_path = []
        for code in codes:
            code_path = []
            for char in code:
                char_code = []
                if keypad2[start2] == char:
                    code_path.append(["A"])
                    continue
                paths = [[[], [start2]]]
                while True:
                    temp_paths = []
                    for path in paths:
                        (x, y) = path[1][-1]
                        for i, j, c in [(1, 0, "v"), (-1, 0, "^"), (0, -1, "<"), (0, 1, ">")]:
                            if (x + i, y + j) in keypad2:
                                temp_path = list(path[1])
                                temp_code = list(path[0])
                                temp_path.append((x + i, y + j))
                                temp_code.append(c)
                                if keypad2[(x + i, y + j)] == char:
                                    temp_code.append("A")
                                    char_code.append("".join(temp_code))
                                    start2 = (x + i, y + j)
                                temp_paths.append([list(temp_code), list(temp_path)])
                    else:
                        paths = temp_paths
                        if char_code:
                            code_path.append(char_code)
                            break
                        continue
            codes_path.append(code_path)
        outer_codes_path.append(codes_path)
    robot3.append(outer_codes_path)

combs_outer_outer = []
for robot in robot3:
    combs_outer = []
    for rob in robot:
        combs = []
        for code in rob:
            prev = list(code[0])
            for i in range(1, len(code)):
                t1 = []
                for j in code[i]:
                    for t2 in prev:
                        t1.append("".join(t2) + j)
                prev = t1
            combs.append(prev)
        combs_outer.append(combs)
    combs_outer_outer.append(combs_outer)
robot3 = combs_outer_outer

for i, robot in enumerate(robot3):
    minlen = 9999
    for rob in robot:
        for ro in rob:
            for r in ro:
                if len(r) < minlen:
                    minlen = len(r)
    answer1 += minlen * int("".join([x for x in input_list[i] if x.isdigit()]))

print("Answer 1:", answer1)
print("Answer 2:", answer2)
