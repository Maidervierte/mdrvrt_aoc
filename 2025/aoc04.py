""" 2025 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

paper = set()
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "@":
            paper.add((i, j))

for x,y in paper:
    adjacent=0
    for i,j in [(x+1,y),(x,y+1),(x+1,y+1),(x-1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]:
        if (i,j) in paper:
            adjacent+=1
    if adjacent<4:
        answer1 += 1

answer2=len(paper)

for _ in range(len(input_list)):
    remove=set()
    for x,y in paper:
        adjacent=0
        for i,j in [(x+1,y),(x,y+1),(x+1,y+1),(x-1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]:
            if (i,j) in paper:
                adjacent+=1
        if adjacent<4:
            remove.add((x,y))
    paper = paper - remove

answer2-=len(paper)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
