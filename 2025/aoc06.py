""" 2025 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

numbers = []
for i, line in enumerate(input_list[:-1]):
    for j, number in enumerate([int(x) for x in line.split()]):
        if len(numbers) <= j:
            numbers.append([0] * (len(input_list) - 1))
        numbers[j][i] = number

for i, operation in enumerate(input_list[-1].strip().split()):
    if operation == "+":
        for number in numbers[i]:
            answer1 += number
    if operation == "*":
        temp = 1
        for number in numbers[i]:
            temp *= number
        answer1 += temp

operations = []
lengths = []
cur_len = 0
for i, char in enumerate(input_list[-1]):
    if char != " ":
        operations.append(char)
        lengths.append((i - cur_len - 1))
        cur_len = i
lengths.append((len(input_list[-1]) - cur_len))
lengths.pop(0)

i = 0
for i, length in enumerate(lengths):
    spaced = [""] * (len(input_list) - 1)
    for j in range(length):
        for k in range(len(input_list) - 1):
            spaced[k] += input_list[k][sum(lengths[:i]) + j + i]
    temp = [""] * (len(input_list) - 1)
    for number in spaced:
        for j, char in enumerate(number):
            if number != " ":
                temp[j] += char
    if operations[i] == "+":
        for number in temp:
            if number != "":
                answer2 += int(number)
    if operations[i] == "*":
        temp_num = 1
        for number in temp:
            if number != "":
                temp_num *= int(number)
        answer2 += temp_num

print("Answer 1:", answer1)
print("Answer 2:", answer2)
