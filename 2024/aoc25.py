""" 2024 aoc25"""

with open("input25.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split("\n\n")

answer1 = 0
answer2 = 0
keys = {}
locks = {}

for k, schematic in enumerate(input_list):
    schematic = schematic.splitlines()
    # print(k, schematic)
    if schematic[0][0] == ".":
        key = set()
        for i, line in enumerate(schematic):
            for j, char in enumerate(line):
                if char == "#":
                    key.add((i, j))
        keys[k] = key
    else:
        lock = set()
        for i, line in enumerate(schematic):
            for j, char in enumerate(line):
                if char == "#":
                    lock.add((i, j))
        locks[k] = lock

for lock in locks.values():
    for key in keys.values():
        fit = lock.intersection(key)
        if not fit:
            answer1 += 1

print("Answer 1:", answer1)
