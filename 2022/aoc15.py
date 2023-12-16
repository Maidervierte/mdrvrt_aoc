""" 2022 aoc15 """
with open("input15.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

sensors = {}
for line in input_list:
    sensors[(int(line.split(": closest beacon is at x=")[0][12:].split(", y=")[0]),
             int(line.split(": closest beacon is at x=")[0][12:].split(", y=")[1]))] = (
        int(line.split(": closest beacon is at x=")[1].split(", y=")[0]),
        int(line.split(": closest beacon is at x=")[1].split(", y=")[1]))

row, max_row = 2000000, 4000000
blocked = set()
for sensor, beacon in sensors.items():
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    if abs(sensor[1] - row) <= distance:
        for x in range(sensor[0] - (distance - abs(sensor[1] - row)),
                       sensor[0] + (distance - abs(sensor[1] - row)) + 1): blocked.add(x)
answer1, answer2 = len(blocked) - 1, 0
for sensor, beacon in sensors.items():
    if answer2 != 0:
        break
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    x, y = distance + 2, -1
    outofrange = False
    cur_overlap = []
    for sensor2, beacon2 in sensors.items():
        if sensor == sensor2:
            continue
        distance2 = abs(sensor2[0] - beacon2[0]) + abs(sensor2[1] - beacon2[1])
        dist_sens = abs(sensor[0] - sensor2[0]) + abs(sensor[1] - sensor2[1])
        if (distance + distance2) >= dist_sens > distance:
            cur_overlap.append((sensor2, beacon2))
    while not outofrange:
        x -= 1
        if x >= 0: y += 1
        if x < 0: y -= 1
        outofrange = True
        if (sensor[0] + x) > max_row or (sensor[0] + x) < 0 or (sensor[1] + y) > max_row or (
                sensor[1] + y) < 0: continue
        for (sensor2, beacon2) in cur_overlap:
            if (abs(sensor2[0] - (sensor[0] + x)) + abs(sensor2[1] - (sensor[1] + y))) <= (
                    abs(sensor2[0] - beacon2[0]) + abs(sensor2[1] - beacon2[1])):
                outofrange = False
                break
        if outofrange:
            answer2 = (sensor[0] + x) * 4000000 + sensor[1] + y
        if x == -(distance + 2):
            break

print("Answer 1:", answer1)
print("Answer 2:", answer2)
