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
min_loc = 9999999999999999999
for seed in seeds:
    for line in soil_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= seed <= source_range_start + range_length:
            soil = dest_range_start + (seed - source_range_start)
            break
    for line in fert_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= soil <= source_range_start + range_length:
            fert = dest_range_start + (soil - source_range_start)
            break
    for line in water_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= fert <= source_range_start + range_length:
            water = dest_range_start + (fert - source_range_start)
            break
    for line in light_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= water <= source_range_start + range_length:
            light = dest_range_start + (water - source_range_start)
            break
    for line in temp_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= light <= source_range_start + range_length:
            temp = dest_range_start + (light - source_range_start)
            break
    for line in hum_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= temp <= source_range_start + range_length:
            hum = dest_range_start + (temp - source_range_start)
            break
    for line in loc_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= hum <= source_range_start + range_length:
            loc = dest_range_start + (hum - source_range_start)
            break
    min_loc = min(min_loc, loc)

print("Answer 1:", min_loc)

seed_ranges = [int(x) for x in input_list[0].split()[1:]]
i = 0
min_loc = 9999999999999999
min_seed = 0
while i < len(seed_ranges):
    for x in range(0, seed_ranges[i + 1], 50000):
        seed = seed_ranges[i] + x
        for line in soil_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= seed <= source_range_start + range_length:
                soil = dest_range_start + (seed - source_range_start)
                break
        for line in fert_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= soil <= source_range_start + range_length:
                fert = dest_range_start + (soil - source_range_start)
                break
        for line in water_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= fert <= source_range_start + range_length:
                water = dest_range_start + (fert - source_range_start)
                break
        for line in light_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= water <= source_range_start + range_length:
                light = dest_range_start + (water - source_range_start)
                break
        for line in temp_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= light <= source_range_start + range_length:
                temp = dest_range_start + (light - source_range_start)
                break
        for line in hum_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= temp <= source_range_start + range_length:
                hum = dest_range_start + (temp - source_range_start)
                break
        for line in loc_input:
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            if source_range_start <= hum <= source_range_start + range_length:
                loc = dest_range_start + (hum - source_range_start)
                break
        if loc < min_loc:
            min_loc = loc
            min_seed = seed
    i += 2

for x in range(min_seed - 60000, min_seed + 60000):
    seed = x
    for line in soil_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= seed <= source_range_start + range_length:
            soil = dest_range_start + (seed - source_range_start)
            break
    for line in fert_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= soil <= source_range_start + range_length:
            fert = dest_range_start + (soil - source_range_start)
            break
    for line in water_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= fert <= source_range_start + range_length:
            water = dest_range_start + (fert - source_range_start)
            break
    for line in light_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= water <= source_range_start + range_length:
            light = dest_range_start + (water - source_range_start)
            break
    for line in temp_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= light <= source_range_start + range_length:
            temp = dest_range_start + (light - source_range_start)
            break
    for line in hum_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= temp <= source_range_start + range_length:
            hum = dest_range_start + (temp - source_range_start)
            break
    for line in loc_input:
        dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
        if source_range_start <= hum <= source_range_start + range_length:
            loc = dest_range_start + (hum - source_range_start)
            break
    if loc < min_loc:
        min_loc = loc
        min_seed = seed

print("Answer 2:", min_loc)
