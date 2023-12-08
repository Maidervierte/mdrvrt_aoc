""" 2023 aoc08 """

import math

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

instructions = list(input_list[0])

nodes = {}
for line in input_list[2:]:
    node, rest = line.split(" = ")
    left, right = rest[1:-1].split(", ")
    nodes[node] = (left, right)

cur_node = "AAA"

steps = 0
i = 0
while True:
    steps += 1
    left, right = nodes[cur_node]
    if instructions[i] == "L":
        cur_node = left
    else:
        cur_node = right
    i += 1
    if i == len(instructions):
        i = 0
    if cur_node == "ZZZ":
        print("Answer 1:", steps)
        break

cur_nodes = []
for node in nodes:
    if node[-1] == "A":
        cur_nodes.append(node)

lcm = set()
for cur_node in cur_nodes:
    steps = 0
    i = 0
    while True:
        steps += 1
        left, right = nodes[cur_node]
        if instructions[i] == "L":
            cur_node = left
        else:
            cur_node = right
        i += 1
        if i == len(instructions):
            i = 0
        if cur_node[-1] == "Z":
            lcm.add(steps)
            break

print("Answer 2:", math.lcm(*lcm))
