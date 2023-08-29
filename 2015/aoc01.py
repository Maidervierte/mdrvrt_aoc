""" 2015 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    number_list = f.read()

floor = 0
answer2 = 0
for index, x in enumerate(number_list):
    if x == "(":
        floor += 1
    elif x == ")":
        floor -= 1
    if floor == -1 and answer2 == 0:
        answer2 = index + 1

print("Answer 1:", floor)
print("Answer 2:", answer2)
