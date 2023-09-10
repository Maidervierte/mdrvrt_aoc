""" 2017 aoc20 """
from collections import Counter
from tqdm import tqdm

with open("input20.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

particles = {}
min_accel = len(input_list) * len(input_list)
for i, line in enumerate(input_list):
    line_split = line.split(", ")
    p1, p2, p3 = tuple(int(x) for x in line_split[0][3:-1].split(","))
    v1, v2, v3 = tuple(int(x) for x in line_split[1][3:-1].split(","))
    a1, a2, a3 = tuple(int(x) for x in line_split[2][3:-1].split(","))
    particles[i] = ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3))
    if min_accel > min(min_accel, sum([abs(a1), abs(a2), abs(a3)])):
        closest = i
        min_accel = sum([abs(a1), abs(a2), abs(a3)])
print("Answer 1:", closest)

to_remove = set()
positions = [(p1, p2, p3) for ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3)) in particles.values()]
positions_counter = Counter(positions)

for key, ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3)) in particles.items():
    if positions_counter[(p1, p2, p3)] != 1:
        to_remove.add(key)

for key in to_remove:
    particles.pop(key)

i = 0
while i < 100:
    i += 1
    to_remove = set()
    for key, ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3)) in particles.items():
        particles[key] = ((p1 + v1 + a1, p2 + v2 + a2, p3 + v3 + a3), (v1 + a1, v2 + a2, v3 + a3), (a1, a2, a3))
    positions = [(p1, p2, p3) for ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3)) in particles.values()]
    positions_counter = Counter(positions)
    for key, ((p1, p2, p3), (v1, v2, v3), (a1, a2, a3)) in particles.items():
        if positions_counter[(p1, p2, p3)] != 1:
            to_remove.add(key)
    for key in to_remove:
        particles.pop(key)

print("Answer 2:", len(particles))
