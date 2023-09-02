""" 2016 aoc03 """
with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

number_list = []
for x in input_list:
    temp1 = x.split(" ")
    temp2 = []
    for y in temp1:
        if y != "":
            temp2.append(int(y))
    number_list.append(temp2)

possibles = 0
possibles2 = 0
for x in number_list:
    incr = True
    if (x[x.index(max(x)) - 1] + x[x.index(max(x)) - 2]) <= max(x):
        continue
    possibles += 1

for x in range(0, len(number_list) - 2, 3):
    for y in range(3):
        z = [number_list[x][y], number_list[x + 1][y], number_list[x + 2][y]]
        if (z[z.index(max(z)) - 1] + z[z.index(max(z)) - 2]) <= max(z):
            continue
        possibles2 += 1

print("Answer 1:", possibles)
print("Answer 2:", possibles2)
