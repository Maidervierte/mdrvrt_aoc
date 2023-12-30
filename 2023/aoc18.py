""" 2023 aoc18 """

with open("input18.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

dig_plan = []
for i, line in enumerate(input_list):
    direction = line.split(" ")[0]
    meters = int(line.split(" ")[1])
    colour = line.split(" ")[2][1:-1]
    dig_plan.append((direction, meters, colour))

lagoon = {}
cur_pos = (0, 0)
answer1 = 0
for direction, meters, colour in dig_plan:
    # print(direction, meters, cur_pos)
    x, y = cur_pos
    match direction:
        case "R":
            for y in range(y + 1, y + meters + 1):
                answer1 += 1
                cur_pos = x, y
                lagoon[cur_pos] = "#"
        case "L":
            for y in range(y - 1, y - meters - 1, -1):
                answer1 += 1
                cur_pos = x, y
                lagoon[cur_pos] = "#"
        case "U":
            for x in range(x - 1, x - meters - 1, -1):
                answer1 += 1
                cur_pos = x, y
                lagoon[cur_pos] = "#"
        case "D":
            for x in range(x + 1, x + meters + 1):
                answer1 += 1
                cur_pos = x, y
                lagoon[cur_pos] = "#"

in_lagoon = (1, 1)

# for i in range(-4, 4):
#     for j in range(-4, 4):
#         if (i, j) == in_lagoon:
#             print("O", end="")
#         elif (i, j) in lagoon:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

queue = [in_lagoon]
visited = set()
visited.add(in_lagoon)
answer1 += 1
while len(queue) != 0:
    i, j = queue.pop()
    for x in [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1),
              (i, j + 1),
              (i + 1, j + 1)]:
        if x not in lagoon and x not in visited:
            visited.add(x)
            queue.append(x)
            answer1 += 1
print("Answer 1:", answer1)

answer2 = 0
cur_pos = (0, 0)
for i, (_, _, colour) in enumerate(dig_plan):
    # print(cur_pos)
    match colour[-1]:
        case "0":
            direction = "R"
        case "1":
            direction = "D"
        case "2":
            direction = "L"
        case "3":
            direction = "U"
    meters = int(colour[1:-1], 16)
    x1, y1 = cur_pos
    x2, y2 = cur_pos
    match direction:
        case "R":
            x2 += meters
        case "L":
            x2 -= meters
        case "U":
            y2 -= meters
        case "D":
            y2 += meters
    answer2 += x1 * y2 - x2 * y1
    answer2 += meters
    cur_pos = (x2, y2)

print("Answer 2:",1+answer2 // 2)
