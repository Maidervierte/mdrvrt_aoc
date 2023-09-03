""" 2016 aoc09 """
import re

with open("input09.txt", "r", encoding="utf-8") as f:
    _input = f.read()

decomp = ""
repeated = [-1]
markers = re.finditer(r'\(\d+x\d+\)', _input)
for marker in markers:
    marker_start = marker.span()[0]
    if marker_start < repeated[-1]:
        continue
    marker_end = marker.span()[1]
    to_repeat = int(marker[0].split("x")[0][1:])
    repeats = int(marker[0].split("x")[1][:-1])
    for i in range(max(repeated[-1], 0), marker_start):
        decomp += _input[i]
    for i in range(repeats):
        for j in range(marker_end, marker_end + to_repeat):
            decomp += _input[j]
    repeated.append(marker_end + to_repeat)

for i in range(repeated[-1], len(_input)):
    decomp += _input[i]

print("Answer 1:", len(decomp))

decomp = 0
repeated = [1 for x in range(len(_input))]
markers = re.finditer(r'\(\d+x\d+\)', _input)
marker_len = 0
for marker in markers:
    marker_start = marker.span()[0]
    marker_end = marker.span()[1]
    to_repeat = int(marker[0].split("x")[0][1:])
    repeats = int(marker[0].split("x")[1][:-1])
    decomp += to_repeat * (repeats - 1) * repeated[marker_start]
    decomp -= len(marker[0]) * (repeated[marker_start] - 1)
    marker_len += len(marker[0])
    for i in range(marker_end, marker_end + to_repeat):
        repeated[i] *= repeats

decomp += len(_input) - marker_len

print("Answer 2:", decomp)
