""" 2018 aoc10 """
with open("input10.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

points = {}
velocities = set()
for i, line in enumerate(input_list):
    line_split = line.split("> velocity=<")
    p_x, p_y = (int(x) for x in line_split[0][10:].split(", "))
    v_x, v_y = (int(x) for x in line_split[1][:-1].split(", "))
    points[i] = ((p_x, p_y), (v_x, v_y))

distance_sum = 0
for (p_x1, p_y1), (v_x1, v_y1) in points.values():
    for (p_x2, p_y2), (v_x2, v_y2) in points.values():
        distance_sum += abs(p_x1 - p_x2) + abs(p_y1 - p_y2)
prev_sum = distance_sum + 1

i = 0
mult = 10000
answer2 = 0
while prev_sum != distance_sum:
    if prev_sum < distance_sum:
        mult /= -10
    answer2 += mult
    prev_sum = distance_sum
    distance_sum = 0
    for p_id, ((p_x1, p_y1), (v_x1, v_y1)) in points.items():
        points[p_id] = ((round(p_x1 + mult * v_x1), round(p_y1 + mult * v_y1)), (v_x1, v_y1))
    for (p_x1, p_y1), (v_x1, v_y1) in points.values():
        for (p_x2, p_y2), (v_x2, v_y2) in points.values():
            distance_sum += abs(p_x1 - p_x2) + abs(p_y1 - p_y2)

for p_id, ((p_x1, p_y1), (v_x1, v_y1)) in points.items():
    points[p_id] = ((p_x1 - v_x1, p_y1 - v_y1), (v_x1, v_y1))

min_x = 999999
min_y = 999999
max_x = 0
max_y = 0
for p_id, ((p_x1, p_y1), (v_x1, v_y1)) in points.items():
    min_x = min(min_x, p_x1)
    min_y = min(min_y, p_y1)
    max_x = max(max_x, p_x1)
    max_y = max(max_y, p_y1)

points_set = set()
for p_id, ((p_x1, p_y1), (v_x1, v_y1)) in points.items():
    points_set.add((p_x1 - min_x, p_y1 - min_y))

for y in range(-1, max_y - min_y + 2):
    for x in range(-1, max_x - min_x + 2):
        if (x, y) in points_set:
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()
# GPJLLLLH

print("Answer 2:", answer2)  # rounded down
