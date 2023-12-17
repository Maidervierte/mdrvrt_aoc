""" 2019 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

wire1 = input_list[0].split(",")
wire2 = input_list[1].split(",")

cur_pos = (0, 0)
visited_w1 = set()
visited_w1_2 = set()
i = 1
for path in wire1:
    match path[0]:
        case "R":
            for x in range(cur_pos[0]+1, cur_pos[0] + int(path[1:]) + 1):
                cur_pos = (x, cur_pos[1], i)
                i += 1
                visited_w1.add(cur_pos)
                visited_w1_2.add((cur_pos[0], cur_pos[1]))
        case "L":
            for x in range(cur_pos[0]-1, cur_pos[0] - int(path[1:]) - 1, -1):
                cur_pos = (x, cur_pos[1], i)
                i += 1
                visited_w1.add(cur_pos)
                visited_w1_2.add((cur_pos[0], cur_pos[1]))
        case "U":
            for y in range(cur_pos[1]+1, cur_pos[1] + int(path[1:]) + 1):
                cur_pos = (cur_pos[0], y, i)
                i += 1
                visited_w1.add(cur_pos)
                visited_w1_2.add((cur_pos[0], cur_pos[1]))
        case "D":
            for y in range(cur_pos[1]-1, cur_pos[1] - int(path[1:]) - 1, -1):
                cur_pos = (cur_pos[0], y, i)
                i += 1
                visited_w1.add(cur_pos)
                visited_w1_2.add((cur_pos[0], cur_pos[1]))

cur_pos = (0, 0)
visited_w2 = set()
visited_w2_2 = set()
i = 1
for path in wire2:
    match path[0]:
        case "R":
            for x in range(cur_pos[0]+1, cur_pos[0] + int(path[1:]) + 1):
                cur_pos = (x, cur_pos[1], i)
                i += 1
                visited_w2.add(cur_pos)
                visited_w2_2.add((cur_pos[0], cur_pos[1]))
        case "L":
            for x in range(cur_pos[0]-1, cur_pos[0] - int(path[1:]) - 1, -1):
                cur_pos = (x, cur_pos[1], i)
                i += 1
                visited_w2.add(cur_pos)
                visited_w2_2.add((cur_pos[0], cur_pos[1]))
        case "U":
            for y in range(cur_pos[1]+1, cur_pos[1] + int(path[1:]) + 1):
                cur_pos = (cur_pos[0], y, i)
                i += 1
                visited_w2.add(cur_pos)
                visited_w2_2.add((cur_pos[0], cur_pos[1]))
        case "D":
            for y in range(cur_pos[1]-1, cur_pos[1] - int(path[1:]) - 1, -1):
                cur_pos = (cur_pos[0], y, i)
                i += 1
                visited_w2.add(cur_pos)
                visited_w2_2.add((cur_pos[0], cur_pos[1]))

answer1 = 9999
intersections = visited_w1_2.intersection(visited_w2_2)
for x, y in intersections:
    if (x, y) != (0, 0):
        answer1 = min(answer1, abs(x) + abs(y))

print("Answer 1:", answer1)

visited_w1 = [(x, y, i) for (x, y, i) in visited_w1 if (x, y) in intersections]
visited_w2 = [(x, y, i) for (x, y, i) in visited_w2 if (x, y) in intersections]

answer2 = 9999
for x1, y1, i1 in visited_w1:
    for x2, y2, i2 in visited_w2:
        if (x1, y1) == (x2, y2) and i1 != 0:
            answer2 = min(answer2, i1 + i2)

print("Answer 2:", answer2)
