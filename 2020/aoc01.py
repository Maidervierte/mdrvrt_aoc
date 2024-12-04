""" 2020 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().splitlines()]

answer1 = 0
for x in input_list:
    for y in input_list:
        if (x + y) == 2020:
            answer1 = x * y
            break
    else:
        continue
    break
print("Answer 1:", answer1)

answer2 = 0
for x in input_list:
    for y in input_list:
        for z in input_list:
            if (x + y + z) == 2020:
                answer2 = x * y * z
                break
        else:
            continue
        break
    else:
        continue
    break
print("Answer 2:", answer2)
