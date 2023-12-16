""" 2022 aoc04 """
with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

numberlist = []
for x in input_list:
    temp = x.replace("-", ",").split(",")
    temp2 = []
    for y in temp:
        temp2.append(int(y))
    numberlist.append(temp2)
contained, contained2 = 0, 0
for x in numberlist:
    if x[0] >= x[2]:
        if x[1] <= x[3]:
            contained += 1
            continue
    if x[2] >= x[0]:
        if x[3] <= x[1]:
            contained += 1
            continue
for x in numberlist:
    temp_set1, temp_set2 = set(), set()
    for y in range(x[0], x[1] + 1):
        temp_set1.add(y)
    for y in range(x[2], x[3] + 1):
        temp_set2.add(y)
    if len(temp_set1.intersection(temp_set2)) > 0:
        contained2 += 1

print("Answer 1:", contained)
print("Answer 2:", contained2)
