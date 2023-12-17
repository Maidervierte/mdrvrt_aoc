""" 2019 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = sum([int(x) // 3 - 2 for x in input_list])
print("Answer 1:", answer1)

answer2 = 0
for module in input_list:
    module = int(module)
    module = module // 3 - 2
    while module >= 0:
        answer2 += module
        module = module // 3 - 2

print("Answer 2:", answer2)
