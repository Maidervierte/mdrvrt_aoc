""" 2015 aoc10 """

import time

with open("input10.txt", "r", encoding="utf-8") as f:
    sequence = f.read()

# sequence = "1"
quots = []
for _ in range(50):
    tic = time.perf_counter()
    if _ == 40:
        print("Answer 1: " + str(len(sequence)))
    count = 1
    cur = sequence[0]
    temp = ""
    for i in range(1, len(sequence)):
        if sequence[i] == cur:
            count += 1
        else:
            temp += str(count) + cur
            count = 1
            cur = sequence[i]
    if count != 0:
        temp += str(count) + cur
    quots.append(len(temp) / len(sequence))
    sequence = temp
    toc = time.perf_counter()
    print("Iteration "+str(_)+f" took {toc - tic:0.4f} seconds")

print("Answer 2: " + str(len(sequence)))
