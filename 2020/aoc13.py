""" 2020 aoc13 """

with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
start_time = int(input_list[0])
busses = input_list[1].split(",")

cur_time = start_time
while True:
    for bus in busses:
        if not bus.isdigit():
            continue
        bus = int(bus)
        if cur_time % bus == 0:
            answer1 = (cur_time - start_time) * bus
            break
    else:
        cur_time += 1
        continue
    break
print("Answer 1:", answer1)

prod = 1
step1 = []
step2 = []
for bus in [int(bus) for bus in busses if bus.isdigit()]:
    prod *= bus
for bus in [int(bus) for bus in busses if bus.isdigit()]:
    step1.append(prod // bus)
for i in range(len(step1)):
    n = [int(bus) for bus in busses if bus.isdigit()][i]
    m = step1[i]
    u = -1 * (m // n)
    v = 1
    while u * n + v * m != 1:
        if (u * n + v * m) < 1:
            v += 1
            u = -1 * ((v * m) // n)
        else:
            u -= 1
    step2.append(v * m)

answer2 = 0
index = 0
for i, bus in enumerate(busses):
    if bus.isdigit():
        answer2 += ((int(bus) - i) % int(bus)) * step2[index]
        index += 1
answer2 = answer2 % prod
print("Answer 2:", answer2)
