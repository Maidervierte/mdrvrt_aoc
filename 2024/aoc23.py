""" 2024 aoc23"""

with open("input23.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
connections = {}
for i, line in enumerate(input_list):
    com1, com2 = line.split("-")
    if com1 in connections:
        connections[com1].add(com2)
    else:
        temp = set()
        temp.add(com2)
        connections[com1] = temp
    if com2 in connections:
        connections[com2].add(com1)
    else:
        temp = set()
        temp.add(com1)
        connections[com2] = temp

networks = set()
for k, v in connections.items():
    for com1 in v:
        for com2 in connections[com1]:
            if com2 in v:
                networks.add(tuple(sorted([k, com1, com2])))

for network in networks:
    if any(x[0] == "t" for x in network):
        answer1 += 1

max_len = 0
for i, (k, v) in enumerate(connections.items()):
    temp_paths = [[k]]
    paths = []
    while paths != temp_paths:
        paths = list(temp_paths)
        temp_paths = []
        for path in paths:
            temp_set = set(connections[path[0]])
            for com in path:
                temp_set = temp_set.intersection(set(connections[com]))
                if not temp_set:
                    break
            for com in temp_set:
                temp_path = sorted(set(path + [com]))
                if temp_path not in temp_paths:
                    temp_paths.append(temp_path)
                if len(temp_path) > max_len:
                    max_len = len(temp_path)
                    answer2 = ",".join(temp_path)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
