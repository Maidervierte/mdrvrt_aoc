""" 2020 aoc15"""

with open("input15.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split(",")]

turn = 1
numbers = {}
new_num = True
last_num = -1
cur_num = -1
for cur_num in input_list:
    if cur_num not in numbers:
        numbers[cur_num] = [turn]
    else:
        numbers[cur_num].append(turn)
    last_num = cur_num
    turn += 1

while turn <= 2020:
    if len(numbers[last_num]) < 2:
        cur_num = 0
    else:
        numbers[last_num] = numbers[last_num][-2:]
        cur_num = numbers[last_num][-1] - numbers[last_num][-2]
    if cur_num not in numbers:
        numbers[cur_num] = [turn]
    else:
        numbers[cur_num].append(turn)
    last_num = cur_num
    turn += 1
answer1 = cur_num
print("Answer 1:", answer1)

turn = 1
numbers = {}
new_num = True
last_num = -1
cur_num = -1
for cur_num in input_list:
    if cur_num not in numbers:
        numbers[cur_num] = [turn]
    else:
        numbers[cur_num].append(turn)
    last_num = cur_num
    turn += 1

while turn <= 30000000:
    if len(numbers[last_num]) < 2:
        cur_num = 0
    else:
        numbers[last_num] = numbers[last_num][-2:]
        cur_num = numbers[last_num][-1] - numbers[last_num][-2]
    if cur_num not in numbers:
        numbers[cur_num] = [turn]
    else:
        numbers[cur_num].append(turn)
    last_num = cur_num
    turn += 1

answer2 = cur_num
print("Answer 2:", answer2)
