""" 2025 aoc08 """
from math import sqrt

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

junctions = {}
connected = {}
for i, line in enumerate(input_list):
    junctions[i] = tuple(int(x) for x in line.split(","))
    connected[i] = set()
    connected[i].add(i)

dists = {}
skip = set()
pairs = set()
for i, (x1, y1, z1) in junctions.items():
    for j, (x2, y2, z2) in junctions.items():
        if j <= i:
            continue
        dists[i, j] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

order = sorted(dists.keys(), key=dists.get)

for _ in range(1000):
    (i, j) = order.pop(0)
    if i in connected[j]:
        continue
    pairs.add((i, j))
    connected[i].add(j)
    connected[j].add(i)
    for k, v in connected.items():
        for i in v:
            for j in v:
                connected[i].add(j)
circuits = set()
for k in sorted(connected, key=lambda k: len(connected[k]), reverse=True):
    circuits.add(tuple(sorted(connected[k])))
answer1 = (len(sorted(circuits, key=len)[-1])
           * len(sorted(circuits, key=len)[-2])
           * len(sorted(circuits, key=len)[-3]))

connected = {}
for i, line in enumerate(input_list):
    connected[i] = set()
    connected[i].add(i)

lc = set()
order = sorted(dists.keys(), key=dists.get)
for _ in range(10000000):
    (i, j) = order.pop(0)
    lc.add(i)
    lc.add(j)
    if len(lc) == len(input_list):
        answer2 = junctions[i][0] * junctions[j][0]
        break

print("Answer 1:", answer1)
print("Answer 2:", answer2)
