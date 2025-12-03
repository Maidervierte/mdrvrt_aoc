""" 2025 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = [x.split("   ") for x in f.read().splitlines()]

answer1 = 0
answer2 = 0

dial = 50
for line in input_list:
    if line[0][0] == "L":
        for i in range( int(line[0][1:])):
            dial-=1
            if dial<0:
                dial=99
            if dial == 0:
                answer2+=1
    if line[0][0] == "R":
        for i in range( int(line[0][1:])):
            dial+=1
            if dial>99:
                dial=0
            if dial == 0:
                answer2+=1
    if dial == 0:
        answer1 += 1

if dial == 0:
    answer2 += 1

print("Answer 1:", answer1)
print("Answer 2:", answer2)
