""" 2024 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read()

input_list = input_list.split("mul(")

answer1 = 0
answer2 = 0
do = True

for line in input_list:
    splitline = line.split(",")
    if len(splitline) > 1:
        lefthand = splitline[0]
        if ")" not in splitline[1]:
            continue
        righthand = splitline[1].split(")")[0]
        if lefthand.isdigit() is False or righthand.isdigit() is False:
            continue
        answer1 += (int(lefthand) * int(righthand))
        if do:
            answer2 += (int(lefthand) * int(righthand))
    if "do()" in line:
        do = True
    if "don't()" in line:
        do = False

print("Answer 1:", answer1)
print("Answer 2:", answer2)
