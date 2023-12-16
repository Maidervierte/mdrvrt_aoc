""" 2022 aoc19 """
with open("input19.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def next_minute(minute, blueprint, index, ores, robots, forbidden):
    if blueprints_max[index] < ores[3]: blueprints_max[index] = ores[3]
    if minute > max_minute or (
            robots[3] == 0 and (ores[3] + sum(range((max_minute - minute) + 1))) <= blueprints_max[index]):
        return
    if ores[0] >= blueprint[3][0] and ores[2] >= blueprint[3][1]:
        next_minute(minute + 1, blueprint, index,
                    [ores[0] - blueprint[3][0] + robots[0], ores[1] + robots[1], ores[2] - blueprint[3][1] + robots[2],
                     ores[3] + robots[3]], [robots[0], robots[1], robots[2], robots[3] + 1], [False, False, False])
    else:
        if ores[0] >= blueprint[2][0] and ores[1] >= blueprint[2][1] and robots[2] < blueprint[3][1] and not forbidden[
            2]:
            next_minute(minute + 1, blueprint, index,
                        [ores[0] - blueprint[2][0] + robots[0], ores[1] - blueprint[2][1] + robots[1],
                         ores[2] + robots[2], ores[3] + robots[3]], [robots[0], robots[1], robots[2] + 1, robots[3]],
                        [False, False, False])
            forbidden[2] = True
        if ores[0] >= blueprint[1] and robots[1] < blueprint[2][1] and not forbidden[1]:
            next_minute(minute + 1, blueprint, index,
                        [ores[0] - blueprint[1] + robots[0], ores[1] + robots[1], ores[2] + robots[2],
                         ores[3] + robots[3]], [robots[0], robots[1] + 1, robots[2], robots[3]], [False, False, False])
            forbidden[1] = True
        if ores[0] >= blueprint[0] and robots[0] < max(blueprint[1], blueprint[2][0], blueprint[3][0]) and not \
                forbidden[0]:
            next_minute(minute + 1, blueprint, index,
                        [ores[0] - blueprint[0] + robots[0], ores[1] + robots[1], ores[2] + robots[2],
                         ores[3] + robots[3]], [robots[0] + 1, robots[1], robots[2], robots[3]], [False, False, False])
            forbidden[0] = True
        if ores[0] < (max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]) + 1):
            next_minute(minute + 1, blueprint, index,
                        [ores[0] + robots[0], ores[1] + robots[1], ores[2] + robots[2], ores[3] + robots[3]], robots,
                        forbidden)


blueprints, max_minute = [], 24
for line in input_list:
    blueprints.append(
        [int(line.split(" ")[6]), int(line.split(" ")[12]), (int(line.split(" ")[18]), int(line.split(" ")[21])),
         (int(line.split(" ")[27]), int(line.split(" ")[30]))])
blueprints_max = [0] * len(blueprints)

for index, blueprint in enumerate(blueprints):
    next_minute(1, blueprint, index, [0, 0, 0, 0], [1, 0, 0, 0],
                [False, False, False])
answer1, answer2, max_minute = 0, 1, 32
for i, x in enumerate(blueprints_max):
    answer1 += (i + 1) * x

for index, blueprint in enumerate(blueprints[:3]):
    next_minute(1, blueprint, index, [0, 0, 0, 0], [1, 0, 0, 0],
                [False, False, False])
for x in blueprints_max[:3]:
    answer2 *= x

print("Answer 1:", answer1)
print("Answer 2:", answer2)
