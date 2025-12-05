""" 2025 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

ranges = []
ids = []
for i, line in enumerate(input_list):
    if "-" in line:
        ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
    elif line != "":
        ids.append(int(line))

for i in ids:
    for x, y in ranges:
        if x <= i <= y:
            answer1 += 1
            break

ranges=set(ranges)
for _ in range(len(ranges)*10):
    added=set()
    new_ranges = set()
    for x1,y1 in ranges:
        for x2,y2 in ranges:
            if (x1,y1) in added or (x2,y2) in added or (x1==x2 and y1==y2):
                continue
            if x1<=x2<=y1:
                new_ranges.add((x1,max(y1,y2)))
                added.add((x1,y1))
                added.add((x2,y2))
    for x,y in ranges-added:
        new_ranges.add((x,y))
    ranges=new_ranges

for x,y in ranges:
    answer2+=y-x+1

print("Answer 1:", answer1)
print("Answer 2:", answer2)
