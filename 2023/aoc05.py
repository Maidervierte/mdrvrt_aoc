""" 2023 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

inputs = []
cur_input = []
for line in input_list[3:]:
    if line == "":
        continue
    if not line[0].isdigit():
        inputs.append(cur_input)
        cur_input = []
    else:
        cur_input.append([int(x) for x in line.split()])
inputs.append(cur_input)

seeds = [int(x) for x in input_list[0].split()[1:]]
min_loc = 9999999999999999999
for item in seeds:
    for input_map in inputs:
        for line in input_map:
            dest_range_start, source_range_start, range_length = line
            if source_range_start <= item <= source_range_start + range_length:
                item = dest_range_start + (item - source_range_start)
                break
    min_loc = min(min_loc, item)

print("Answer 1:", min_loc)

seed_ranges = [int(x) for x in input_list[0].split()[1:]]
i = 0
min_loc = 9999999999999999
min_seed = 0
while i < len(seed_ranges):
    for x in range(0, seed_ranges[i + 1], 50000):
        seed = seed_ranges[i] + x
        item = seed
        for input_map in inputs:
            for line in input_map:
                dest_range_start, source_range_start, range_length = line
                if source_range_start <= item <= source_range_start + range_length:
                    item = dest_range_start + (item - source_range_start)
                    break
        if item < min_loc:
            min_loc = item
            min_seed = seed
    i += 2

for item in range(min_seed - 50000, min_seed + 50000):
    for input_map in inputs:
        for line in input_map:
            dest_range_start, source_range_start, range_length = line
            if source_range_start <= item <= source_range_start + range_length:
                item = dest_range_start + (item - source_range_start)
                break
    min_loc = min(min_loc, item)

print("Answer 2:", min_loc)
