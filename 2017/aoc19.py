""" 2017 aoc19 """

with open("input19.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

maze = {}
for i, char in enumerate(input_list[0]):
    if char == "|":
        start = (0, i)

letters = 0
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char != " ":
            maze[(i, j)] = char
            if char.isupper():
                letters += 1

visited = set()
visited.add(start)
prev = (0, 0)
cur_pos = start
cur_sign = "|"
answer1 = ""
debug = False
steps = 1
while len(answer1) < letters:
    steps += 1
    # print(cur_pos, maze[cur_pos], answer1)
    # if cur_pos==(31,118) or debug:
    #     for x in range(len(input_list)):
    #         for y in range(len(input_list[0])):
    #             if (x, y) == cur_pos:
    #                 print("#", end="")
    #             elif (x, y) in maze:
    #                 print(maze[(x, y)], end="")
    #             else:
    #                 print(" ", end="")
    #         print()
    #     debug=True
    x, y = cur_pos
    possible = []
    if cur_sign == "-":
        if (x - 1, y) in maze and maze[(x - 1, y)] != "-" and maze[(x - 1, y)] != "|" and (x - 1, y) != prev:
            possible.append((x - 1, y))
        if (x + 1, y) in maze and maze[(x + 1, y)] != "-" and maze[(x + 1, y)] != "|" and (x + 1, y) != prev:
            possible.append((x + 1, y))
        if (x, y - 1) in maze and (x, y - 1) != prev:
            possible.append((x, y - 1))
        if (x, y + 1) in maze and (x, y + 1) != prev:
            possible.append((x, y + 1))
    elif cur_sign == "|":
        if (x - 1, y) in maze and (x - 1, y) != prev:
            possible.append((x - 1, y))
        if (x + 1, y) in maze and (x + 1, y) != prev:
            possible.append((x + 1, y))
        if (x, y - 1) in maze and maze[(x, y - 1)] != "|" and maze[(x, y - 1)] != "-" and (x, y - 1) != prev:
            possible.append((x, y - 1))
        if (x, y + 1) in maze and maze[(x, y + 1)] != "|" and maze[(x, y + 1)] != "-" and (x, y + 1) != prev:
            possible.append((x, y + 1))
    if len(possible) == 1:
        prev = cur_pos
        cur_pos = possible[0]
        if maze[possible[0]] == "+" and cur_sign == "-":
            cur_sign = "|"
        elif maze[possible[0]] == "+":
            cur_sign = "-"
        if maze[possible[0]].isupper():
            answer1 += maze[possible[0]]
    else:
        found = False
        prev = cur_pos
        for pos_pos in possible:
            if maze[pos_pos] == cur_sign:
                cur_pos = pos_pos
                found = True
                break
        if not found:
            for pos_pos in possible:
                if maze[pos_pos] == "+":
                    if cur_sign == "-":
                        cur_sign = "|"
                    else:
                        cur_sign = "-"
                cur_pos = pos_pos
                found = True
                break
        if not found:
            for pos_pos in possible:
                if maze[pos_pos].isupper():
                    cur_pos = pos_pos
                    answer1 += maze[pos_pos]
                    break

print("Answer 1:", answer1)
print("Answer 2:", steps)
