""" 2017 aoc13 """

with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

severity = 0
for line in input_list:
    line_split = line.split(": ")
    if int(line_split[0]) % ((int(line_split[1]) - 1) * 2) == 0:
        severity += int(line_split[0]) * int(line_split[1])
print("Answer 1:", severity)

time = 0
while True:
    caught = False
    for line in input_list:
        line_split = line.split(": ")
        if (time + int(line_split[0])) % ((int(line_split[1]) - 1) * 2) == 0:
            caught = True
            break
    if not caught:
        print("Answer 2:", time)
        break
    time += 1
