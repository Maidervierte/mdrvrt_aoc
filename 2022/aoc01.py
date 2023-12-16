""" 2022 aoc01 """
with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

sumlist = [0]
for line in input_list:
    if line == "":
        sumlist.append(0)
    else:
        sumlist[-1] += int(line)
print("Answer 1:", max(sumlist))
print("Answer 2:", sum(sorted(sumlist)[-3:]))
