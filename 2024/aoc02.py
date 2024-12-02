""" 2024 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = [[int(y) for y in x.split(" ")] for x in f.read().splitlines()]

answer1 = 0

for report in input_list:
    if report != sorted(report) and report != sorted(report, reverse=True):
        continue
    safe = True
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3 or abs(report[i] - report[i + 1]) < 1:
            safe = False
            break
    if safe:
        answer1 += 1

print("Answer 1:", answer1)

answer2 = 0

for report in input_list:
    for j in range(len(report)):
        temp = report.copy()
        temp.pop(j)
        if temp != sorted(temp) and temp != sorted(temp, reverse=True):
            continue
        safe = True
        for i in range(len(temp) - 1):
            if abs(temp[i] - temp[i + 1]) > 3 or abs(temp[i] - temp[i + 1]) < 1:
                safe = False
                break
        if safe:
            answer2 += 1
            break

print("Answer 2:", answer2)
