""" 2017 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_blocks = [int(x) for x in f.read().split("	")]

blocks = input_blocks.copy()
seen = set()
seen.add(tuple(blocks))
answer1 = 0
while True:
    for i, x in enumerate(blocks):
        if x == max(blocks):
            index = i
            break
    to_distribute = blocks[index]
    blocks[index] = 0
    for i in range(to_distribute):
        blocks[(1 + index + i) % len(blocks)] += 1
    answer1 += 1
    if tuple(blocks) in seen:
        break
    seen.add(tuple(blocks))
print("Answer 1:", answer1)

blocks = input_blocks.copy()
seen = [tuple(blocks)]
answer1 = 0
while True:
    for i, x in enumerate(blocks):
        if x == max(blocks):
            index = i
            break
    to_distribute = blocks[index]
    blocks[index] = 0
    for i in range(to_distribute):
        blocks[(1 + index + i) % len(blocks)] += 1
    answer1 += 1
    if tuple(blocks) in seen:
        print("Answer 2:", answer1 - seen.index(tuple(blocks)))
        break
    seen.append(tuple(blocks))
