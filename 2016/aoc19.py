""" 2016 aoc19 """
with open("input19.txt", "r", encoding="utf-8") as f:
    elves = int(f.read())

circle = [1 for _ in range(elves)]
index = 0
prev_max = 0
i = 0
prev_index = 0
while True:
    while circle[index] == 0:
        index += 1
        if index >= elves:
            index = 0
    elf1 = index
    index += 1
    if index >= elves:
        index = 0
    while circle[index] == 0:
        index += 1
        if index >= elves:
            index = 0
    elf2 = index
    circle[elf1] += circle[elf2]
    circle[elf2] = 0
    if circle[elf1] == elves:
        break
    index += 1
    if index >= elves:
        index = 0
print("Answer 1:", circle.index(elves) + 1)

circle = [1 for _ in range(elves)]
elf1 = 0
elf2 = elves // 2
skip = True
while True:
    circle[elf1] += circle[elf2]
    if circle[elf1] == elves:
        break
    elf1 += 1
    if elf1 == elves:
        elf1 = 0
    while circle[elf1] == 0:
        elf1 += 1
        if elf1 == elves:
            elf1 = 0
    circle[elf2] = 0
    elf2 += 1
    if elf2 == elves:
        elf2 = 0
    while circle[elf2] == 0:
        elf2 += 1
        if elf2 == elves:
            elf2 = 0
    if skip:
        elf2 += 1
        if elf2 == elves:
            elf2 = 0
        while circle[elf2] == 0:
            elf2 += 1
            if elf2 == elves:
                elf2 = 0
        skip = False
    else:
        skip = True
print("Answer 2:", circle.index(elves) + 1)

# circle = [1 for _ in range(elves)]
# index = 0
# zero_count = 0
# zero_circle = []
# pbar = tqdm(total=elves)
# while True:
#     pbar.update(1)
#     cur_index = index
#     prev_index = index
#     while circle[index] == 0:
#         index += 1
#         if index >= elves:
#             index = 0
#     elf1 = index
#     across = (elves - zero_count) // 2
#     across_counter = 0
#     while across_counter < across:
#         if index + (across - across_counter) < elves:
#             zeroes = bisect.bisect_left(zero_circle, index + (across - across_counter) + 1) - bisect.bisect_left(
#                 zero_circle, index + 1)
#         elif index + 1 < elves:
#             zeroes = bisect.bisect_left(zero_circle, elves) - bisect.bisect_left(zero_circle, index + 1)
#             zeroes += bisect.bisect_left(zero_circle, ((index + across - across_counter + 1) % elves)) - bisect.bisect_left(
#                 zero_circle, 0)
#         else:
#             zeroes = bisect.bisect_left(zero_circle, (across - across_counter)) - bisect.bisect_left(zero_circle, 0)
#         index += (across - across_counter)
#         across_counter += ((across - across_counter) - zeroes)
#         if index >= elves:
#             index = index % elves
#     elf2 = index
#     circle[elf1] += circle[elf2]
#     circle[elf2] = 0
#     bisect.insort(zero_circle, elf2)
#     zero_count += 1
#     if circle[elf1] == elves:
#         break
#     index = elf1 + 1
#     if index >= elves:
#         index = 0
# pbar.close()
# print("Answer 2:", circle.index(elves) + 1)
