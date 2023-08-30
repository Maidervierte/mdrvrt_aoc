""" 2015 aoc14 """
with open("input14.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

reindeer_stats = {}
reindeer_cur = {}
for line in input_lines:
    name, _, _, speed, _, _, dur, _, _, _, _, _, _, rest, _ = line.split(" ")
    reindeer_stats[name] = (int(speed), int(dur), int(rest))
    reindeer_cur[name] = (0, True, int(dur), 0, 0)

for _ in range(2503):
    for reindeer, (dist, go, dur, rest, points) in reindeer_cur.items():
        if go:
            dist += reindeer_stats[reindeer][0]
            dur -= 1
            if dur == 0:
                go = False
                rest = reindeer_stats[reindeer][2]
        else:
            rest -= 1
            if rest == 0:
                go = True
                dur = reindeer_stats[reindeer][1]
        reindeer_cur[reindeer] = (dist, go, dur, rest, points)
    max_dist = 0
    for reindeer, (dist, go, dur, rest, points) in reindeer_cur.items():
        if dist > max_dist:
            max_dist = dist
    for reindeer, (dist, go, dur, rest, points) in reindeer_cur.items():
        if dist == max_dist:
            points += 1
            reindeer_cur[reindeer] = (dist, go, dur, rest, points)

max_points = 0
for reindeer, (dist, go, dur, rest, points) in reindeer_cur.items():
    if points > max_points:
        max_points = points

print("Answer 1:", max_dist)
print("Answer 2:", max_points)
