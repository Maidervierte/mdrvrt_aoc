""" 2017 aoc12 """
import random

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

programs = {}
for line in input_list:
    line_split = line.split(" <-> ")
    programs[int(line_split[0])] = []
    for program in line_split[1].split(", "):
        programs[int(line_split[0])].append(int(program))

visited = set()
visited.add(0)
all_visited = visited.copy()
prev = 0
while len(all_visited) != prev:
    prev = len(all_visited)
    temp_visited = set()
    for program in visited:
        for value in programs[program]:
            temp_visited.add(value)
    visited = temp_visited
    all_visited = all_visited.union(visited)
print("Answer 1:", len(all_visited))

answer2 = 1
for program in all_visited:
    programs.pop(program)
while len(programs.items()) > 0:
    answer2 += 1
    visited = set()
    visited.add(random.choice(list(programs.keys())))
    all_visited = visited.copy()
    prev = 0
    while len(all_visited) != prev:
        prev = len(all_visited)
        temp_visited = set()
        for program in visited:
            for value in programs[program]:
                temp_visited.add(value)
        visited = temp_visited.copy()
        all_visited = all_visited.union(visited)
    for program in all_visited:
        programs.pop(program)

print("Answer 2:", answer2)
