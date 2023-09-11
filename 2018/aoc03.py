""" 2018 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

claimed = set()
already_claimed = set()
counter = 0
# inputlist=["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2",]
for line in input_list:
    temp = line.replace("#", "").replace("@", "").replace(",", " ").replace(":", "").replace("x", " ").split(" ")
    start = (int(temp[2]), int(temp[3]))
    rect = (int(temp[4]), int(temp[5]))
    for x in range(start[0], start[0] + rect[0]):
        for y in range(start[1], start[1] + rect[1]):
            if (x, y) in claimed:
                if (x, y) in already_claimed:
                    continue
                counter += 1
                already_claimed.add((x, y))
            else:
                claimed.add((x, y))
print("Answer 1:", counter)
for line in input_list:
    temp = line.replace("#", "").replace("@", "").replace(",", " ").replace(":", "").replace("x", " ").split(" ")
    start = (int(temp[2]), int(temp[3]))
    rect = (int(temp[4]), int(temp[5]))
    claim = False
    for x in range(start[0], start[0] + rect[0]):
        for y in range(start[1], start[1] + rect[1]):
            if (x, y) in already_claimed:
                claim = True
    if not claim:
        print("Answer 2:", temp[0])

# for x in range(1):
#     for y in range(1):
#         if (y, x) in claimed:
#             print("x", end="")
#         else:
#             print("_", end="")
#     print()
