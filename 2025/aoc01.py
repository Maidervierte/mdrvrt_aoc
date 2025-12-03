""" 2025 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = [x.split("   ") for x in f.read().splitlines()]

list1 = []
list2 = []

for line in input_list:
    list1.append(int(line[0]))
    list2.append(int(line[1]))

answer1 = 0
answer2 = 0
list1.sort()
list2.sort()
for i in range(len(input_list)):
    answer1 += abs(list1[i] - list2[i])
    temp = list2.count(list1[i])
    answer2 += (list1[i] * temp)

print("Answer 1:", answer1)
print("Answer 2:", answer2)