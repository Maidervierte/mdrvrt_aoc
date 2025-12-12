""" 2025 aoc11 """

with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

connections = {}
for line in input_list:
    line_split = line.split(": ")
    connections[line_split[0]] = line_split[1].split(" ")

paths = {"out": 1}
for _ in range(1000):
    # print(paths)
    temp = {}
    for path in paths:
        if path == 'you':
            answer1 += paths[path]
            continue
        for k, v in connections.items():
            if path in v:
                if k in temp:
                    temp[k] += paths[path]
                else:
                    temp[k] = paths[path]
    paths = temp

paths = {("out", 0, 0): 1}
for _ in range(1000):
    # print(paths)
    temp = {}
    for path in paths:
        if path[0] == 'svr' and path[1] and path[2]:
            answer2 += paths[path]
            continue
        for k, v in connections.items():
            _, p1, p2 = path
            if k == 'fft':
                p1 = 1
            if k == 'dac':
                p2 = 1
            if path[0] in v:
                if (k, p1, p2) in temp:
                    temp[(k, p1, p2)] += paths[path]
                else:
                    temp[(k, p1, p2)] = paths[path]
    paths = temp
print("Answer 1:", answer1)
print("Answer 2:", answer2)
