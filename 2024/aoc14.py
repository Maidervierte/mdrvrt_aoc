""" 2024 aoc14"""

with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
wide = 101
tall = 103
robots = []
for i, line in enumerate(input_list):
    line = line.split(" ")
    p = [int(x) for x in line[0].split("=")[1].split(",")]
    v = [int(x) for x in line[1].split("=")[1].split(",")]
    end_pos_x = p[0] + 100 * v[0]
    end_pos_y = p[1] + 100 * v[1]
    if end_pos_x >= wide:
        end_pos_x %= wide
    if end_pos_y >= tall:
        end_pos_y %= tall
    if end_pos_x < 0:
        end_pos_x = (end_pos_x + (((-1 * end_pos_x) // wide) + 1) * wide) % wide
    if end_pos_y < 0:
        end_pos_y = (end_pos_y + (((-1 * end_pos_y) // tall) + 1) * tall) % tall
    end_pos = (end_pos_x, end_pos_y)
    robots.append(end_pos)

q1 = [(x, y) for x in list(range(wide // 2)) for y in list(range(tall // 2))]
q2 = [(x, y) for x in list(range(wide // 2 + 1, wide)) for y in list(range(tall // 2))]
q3 = [(x, y) for x in list(range(wide // 2)) for y in list(range(tall // 2 + 1, tall))]
q4 = [(x, y) for x in list(range(wide // 2 + 1, wide)) for y in list(range(tall // 2 + 1, tall))]
safety = [0, 0, 0, 0]
for y in range(tall):
    for x in range(wide):
        if (x, y) in robots:
            if (x, y) in q1:
                safety[0] += robots.count((x, y))
            if (x, y) in q2:
                safety[1] += robots.count((x, y))
            if (x, y) in q3:
                safety[2] += robots.count((x, y))
            if (x, y) in q4:
                safety[3] += robots.count((x, y))
answer1 = safety[0] * safety[1] * safety[2] * safety[3]
print("Answer 1:", answer1)

robots = {}
for i, line in enumerate(input_list):
    line = line.split(" ")
    p = [int(x) for x in line[0].split("=")[1].split(",")]
    v = [int(x) for x in line[1].split("=")[1].split(",")]
    robots[(tuple(p), tuple(v))] = tuple(p)

for steps in range(wide * tall):
    for (robot, v), p in robots.items():
        end_pos_x = p[0] + v[0]
        end_pos_y = p[1] + v[1]
        if end_pos_x >= wide:
            end_pos_x %= wide
        elif end_pos_x < 0:
            end_pos_x = (end_pos_x + (((-1 * end_pos_x) // wide) + 1) * wide) % wide
        if end_pos_y >= tall:
            end_pos_y %= tall
        elif end_pos_y < 0:
            end_pos_y = (end_pos_y + (((-1 * end_pos_y) // tall) + 1) * tall) % tall
        robots[(robot, v)] = (end_pos_x, end_pos_y)
    temp = set(robots.values())
    for y in range(tall):
        line = ""
        for x in range(wide):
            if (x, y) in temp:
                line += "o"
            else:
                line += "."
        if "ooooooooooooooooooooooooooooooo" in line:
            answer2 += steps+1
            break
    else:
        continue
    break
print("Answer 2:", answer2)
