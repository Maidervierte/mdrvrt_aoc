""" 2020 aoc17"""

with open("input17.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
cubes = set()
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "#":
            cubes.add((i, j, 0))

start = [len(input_list), len(input_list[0]), 0]
for cycle in range(6):
    temp = set(cubes)
    for x in range(-cycle - 1, len(input_list) + cycle + 1):
        for y in range(-cycle - 1, len(input_list) + cycle + 1):
            for z in range(-cycle - 1, cycle + 2):
                if (x, y, z) in cubes:
                    if sum(1 for _x in range(x - 1, x + 2)
                           for _y in range(y - 1, y + 2)
                           for _z in range(z - 1, z + 2)
                           if (_x, _y, _z) in cubes) not in [3, 4]:
                        temp.remove((x, y, z))
                else:
                    if sum(1 for _x in range(x - 1, x + 2)
                           for _y in range(y - 1, y + 2)
                           for _z in range(z - 1, z + 2)
                           if (_x, _y, _z) in cubes) == 3:
                        temp.add((x, y, z))
    cubes = set(temp)
answer1 = len(cubes)
print("Answer 1:", answer1)

cubes = set()
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "#":
            cubes.add((i, j, 0, 0))

start = [len(input_list), len(input_list[0]), 0]
for cycle in range(6):
    temp = set(cubes)
    for x in range(-cycle - 1, len(input_list) + cycle + 1):
        for y in range(-cycle - 1, len(input_list) + cycle + 1):
            for z in range(-cycle - 1, cycle + 2):
                for w in range(-cycle - 1, cycle + 2):
                    if (x, y, z, w) in cubes:
                        if sum(1 for _x in range(x - 1, x + 2)
                               for _y in range(y - 1, y + 2)
                               for _z in range(z - 1, z + 2)
                               for _w in range(w - 1, w + 2)
                               if (_x, _y, _z, _w) in cubes) not in [3, 4]:
                            temp.remove((x, y, z, w))
                    else:
                        if sum(1 for _x in range(x - 1, x + 2)
                               for _y in range(y - 1, y + 2)
                               for _z in range(z - 1, z + 2)
                               for _w in range(w - 1, w + 2)
                               if (_x, _y, _z, _w) in cubes) == 3:
                            temp.add((x, y, z, w))
    cubes = set(temp)
answer2 = len(cubes)
print("Answer 2:", answer2)
