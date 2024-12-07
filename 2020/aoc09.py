""" 2020 aoc09 """

with open("input09.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().splitlines()]

preamble = 25
answer1 = 0
for i, number in enumerate(input_list):
    if i < preamble:
        continue
    prev = []
    for i in range(i - preamble, i):
        prev.append(input_list[i])
    for x in prev:
        for y in prev:
            if x + y == number:
                break
        else:
            continue
        break
    else:
        answer1 = number
        print("Answer 1:", answer1)
        break
    continue

numbers = []
start = 0
stop = 1
num_sum = 0
while True:
    numbers = input_list[start:stop]
    num_sum = sum(numbers)
    if num_sum < answer1:
        stop += 1
    elif num_sum > answer1:
        start += 1
    else:
        break

answer2 = min(numbers) + max(numbers)
print("Answer 2:", answer2)
