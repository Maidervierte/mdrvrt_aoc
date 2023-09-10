""" 2017 aoc01 """

with open("input02.txt", "r", encoding="utf-8") as f:
    inputlist = f.read().splitlines()
numberlist = []
for x in inputlist:
    temp = []
    for y in x.split("\t"):
        temp.append(int(y))
    numberlist.append(temp)
checksum = 0
checksum2 = 0
for x in numberlist:
    checksum += int(max(x)) - int(min(x))
    for ind1, y in enumerate(x):
        for ind2, z in enumerate(x):
            if str((y / z))[-1] == "0" and ind1 != ind2:
                checksum2 += y / z
print("Answer 1:", checksum)
print("Answer 2:", str(checksum2)[:-2])
