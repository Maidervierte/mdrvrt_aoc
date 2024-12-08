""" 2024 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
area = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        area[(i, j)] = char

scanned = set()
antinodes = set()
for key, value in area.items():
    if value == "." or value in scanned:
        continue
    scanned.add(value)
    values = []
    for key2, value2 in area.items():
        if value2 == value:
            values.append(key2)
    for node1 in values:
        for node2 in values:
            if node1 == node2:
                continue
            distance = (abs(node1[0] - node2[0]), abs(node1[1] - node2[1]))
            antinode1_x, antinode1_y, antinode2_x, antinode2_y = -1, -1, -1, -1
            if node1[0] < node2[0]:
                antinode1_x = node1[0] - distance[0]
                antinode2_x = node2[0] + distance[0]
            if node1[0] > node2[0]:
                antinode1_x = node1[0] + distance[0]
                antinode2_x = node2[0] - distance[0]
            if node1[0] == node2[0]:
                antinode1_x = node1[0]
                antinode2_x = node2[0]
            if node1[1] < node2[1]:
                antinode1_y = node1[1] - distance[1]
                antinode2_y = node2[1] + distance[1]
            if node1[1] > node2[1]:
                antinode1_y = node1[1] + distance[1]
                antinode2_y = node2[1] - distance[1]
            if node1[1] == node2[1]:
                antinode1_y = node1[1]
                antinode2_y = node2[1]
            if (antinode1_x, antinode1_y) in area:
                antinodes.add((antinode1_x, antinode1_y))
            if (antinode2_x, antinode2_y) in area:
                antinodes.add((antinode2_x, antinode2_y))
answer1 = len(antinodes)
print("Answer 1:", answer1)

scanned = set()
antinodes = set()
for key, value in area.items():
    if value == "." or value in scanned:
        continue
    scanned.add(value)
    values = []
    for key2, value2 in area.items():
        if value2 == value:
            values.append(key2)
    for node1 in values:
        for node2 in values:
            if node1 == node2:
                continue
            distance = (abs(node1[0] - node2[0]), abs(node1[1] - node2[1]))
            for x in range(-100, 100):
                antinode1_x, antinode1_y, antinode2_x, antinode2_y = -1, -1, -1, -1
                if node1[0] < node2[0]:
                    antinode1_x = node1[0] - distance[0] * x
                    antinode2_x = node2[0] + distance[0] * x
                if node1[0] > node2[0]:
                    antinode1_x = node1[0] + distance[0] * x
                    antinode2_x = node2[0] - distance[0] * x
                if node1[0] == node2[0]:
                    antinode1_x = node1[0]
                    antinode2_x = node2[0]
                if node1[1] < node2[1]:
                    antinode1_y = node1[1] - distance[1] * x
                    antinode2_y = node2[1] + distance[1] * x
                if node1[1] > node2[1]:
                    antinode1_y = node1[1] + distance[1] * x
                    antinode2_y = node2[1] - distance[1] * x
                if node1[1] == node2[1]:
                    antinode1_y = node1[1]
                    antinode2_y = node2[1]
                if (antinode1_x, antinode1_y) in area:
                    antinodes.add((antinode1_x, antinode1_y))
                if (antinode2_x, antinode2_y) in area:
                    antinodes.add((antinode2_x, antinode2_y))
answer2 = len(antinodes)
print("Answer 2:", answer2)
