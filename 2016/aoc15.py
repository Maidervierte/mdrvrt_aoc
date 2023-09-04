""" 2016 aoc15 """

with open("input15.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

discs = {}
for line in input_lines:
    line_split = line.split(" ")
    discs[int(line_split[1][-1])] = (int(line_split[3]), int(line_split[-1][:-1]))

step = 0
time_found = False
while not time_found:
    time = step
    hit = False
    while not hit:
        for disc in sorted(discs):
            time += 1
            positions, start_pos = discs[disc]
            if (time + start_pos) % positions != 0:
                hit = True
                break
        if not hit:
            print("Answer 1:", step)
            time_found = True
            break
    step += 1

discs[7] = (11, 0)
step = 0
time_found = False
while not time_found:
    time = step
    hit = False
    while not hit:
        for disc in sorted(discs):
            time += 1
            positions, start_pos = discs[disc]
            if (time + start_pos) % positions != 0:
                hit = True
                break
        if not hit:
            print("Answer 2:", step)
            time_found = True
            break
    step += 1
