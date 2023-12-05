""" 2023 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

with open("input05sts", "r", encoding="utf-8") as f:
    soil_input = f.read().splitlines()

with open("input05stf", "r", encoding="utf-8") as f:
    fert_input = f.read().splitlines()

with open("input05ftw", "r", encoding="utf-8") as f:
    water_input = f.read().splitlines()

with open("input05wtl", "r", encoding="utf-8") as f:
    light_input = f.read().splitlines()

with open("input05ltt", "r", encoding="utf-8") as f:
    temp_input = f.read().splitlines()

with open("input05tth", "r", encoding="utf-8") as f:
    hum_input = f.read().splitlines()

with open("input05htl", "r", encoding="utf-8") as f:
    loc_input = f.read().splitlines()

seeds = [int(x) for x in input_list[0].split()[1:]]
inputs = [soil_input, fert_input, water_input, light_input, temp_input, hum_input, loc_input]
min_loc = 9999999999999999999
for item in seeds:
    for input_map in inputs:
        for line in input_map:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
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
                dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
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
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= item <= source_range_start + range_length:
                item = dest_range_start + (item - source_range_start)
                break
    min_loc = min(min_loc, item)

print("Answer 2:", min_loc)
