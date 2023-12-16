""" 2022 aoc18 """

with open("input18.txt", "r", encoding="utf-8") as f:
    input_list = f.readlines()

cubes = set()
for line in input_list:
    temp = line.split(",")
    temp = [x.strip() for x in temp]
    temp = [int(x) for x in temp]
    cubes.add(tuple(temp))

sides = 0
max_x, max_y, max_z = 0, 0, 0
for c in cubes:
    if c[0] > max_x:
        max_x = c[0]
    if c[1] > max_y:
        max_y = c[1]
    if c[2] > max_z:
        max_z = c[2]
    if (c[0] + 1, c[1], c[2]) not in cubes:
        sides += 1
    if (c[0] - 1, c[1], c[2]) not in cubes:
        sides += 1
    if (c[0], c[1] + 1, c[2]) not in cubes:
        sides += 1
    if (c[0], c[1] - 1, c[2]) not in cubes:
        sides += 1
    if (c[0], c[1], c[2] + 1) not in cubes:
        sides += 1
    if (c[0], c[1], c[2] - 1) not in cubes:
        sides += 1

answer1 = sides

no_cubes = set()
for x in range(max_x + 1):
    for y in range(max_y + 1):
        for z in range(max_z + 1):
            if (x, y, z) not in cubes:
                no_lava = True
                for x2 in range(x, max_x + 1):
                    if (x2, y, z) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_lava = True
                for x2 in range(x, -1, -1):
                    if (x2, y, z) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_lava = True
                for y2 in range(y, max_y + 1):
                    if (x, y2, z) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_lava = True
                for y2 in range(y, -1, -1):
                    if (x, y2, z) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_lava = True
                for z2 in range(z, max_z + 1):
                    if (x, y, z2) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_lava = True
                for z2 in range(z, -1, -1):
                    if (x, y, z2) in cubes:
                        no_lava = False
                if no_lava:
                    continue
                no_cubes.add((x, y, z))

outside = set()
temp = set()
temp.add((max_x + 1, max_y + 1, max_z + 1))
while temp != outside:
    outside = temp.copy()
    for x, y, z in outside:
        if x < max_x + 2 and (x + 1, y, z) not in cubes:
            temp.add((x + 1, y, z))
        if 0 < x + 2 and (x - 1, y, z) not in cubes:
            temp.add((x - 1, y, z))
        if y < max_x + 2 and (x, y + 1, z) not in cubes:
            temp.add((x, y + 1, z))
        if 0 < y + 2 and (x, y - 1, z) not in cubes:
            temp.add((x, y - 1, z))
        if z < max_x + 2 and (x, y, z + 1) not in cubes:
            temp.add((x, y, z + 1))
        if 0 < z + 2 and (x, y, z - 1) not in cubes:
            temp.add((x, y, z - 1))

for c in outside:
    if c in no_cubes:
        no_cubes.remove(c)

for c in no_cubes:
    if (c[0] + 1, c[1], c[2]) in cubes:
        sides -= 1
    if (c[0] - 1, c[1], c[2]) in cubes:
        sides -= 1
    if (c[0], c[1] + 1, c[2]) in cubes:
        sides -= 1
    if (c[0], c[1] - 1, c[2]) in cubes:
        sides -= 1
    if (c[0], c[1], c[2] + 1) in cubes:
        sides -= 1
    if (c[0], c[1], c[2] - 1) in cubes:
        sides -= 1

answer2 = sides
print("Answer 1:", answer1)
print("Answer 2:", answer2)
