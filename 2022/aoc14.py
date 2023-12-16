""" 2022 aoc14 """
with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

min_y, rockfield = 0, set()

for line in input_list:
    temp = []
    for x in line.split("->"):
        temp.append((int(x.split(",")[0]), int(x.split(",")[1])))
    for index in range(len(temp) - 1):
        for x in range(min(temp[index][0], temp[index + 1][0]), max(temp[index][0], temp[index + 1][0]) + 1):
            for y in range(min(temp[index][1], temp[index + 1][1]), max(temp[index][1], temp[index + 1][1]) + 1):
                if y > min_y:
                    min_y = y
                rockfield.add((x, y))

answer1, answer2, cur_pos = 0, 0, 0
while cur_pos != (500, 0):
    answer2 += 1
    cur_pos = (500, 0)
    while cur_pos not in rockfield:
        if cur_pos[1] > min_y and answer1 == 0: answer1 = answer2 - 1
        for new_pos in [(cur_pos[0], cur_pos[1] + 1), (cur_pos[0] - 1, cur_pos[1] + 1),
                        (cur_pos[0] + 1, cur_pos[1] + 1)]:
            if new_pos not in rockfield and new_pos[1] != min_y + 2:
                cur_pos = new_pos
                break
        if cur_pos != new_pos: rockfield.add(cur_pos)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
