""" 2022 aoc25 """
with open("input25.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

fullsum = 0
for line in input_list:
    linesum = 0
    for i, char in enumerate(reversed(line)):
        if char == "2": x = 2
        if char == "1": x = 1
        if char == "0": x = 0
        if char == "-": x = -1
        if char == "=": x = -2
        linesum += (5 ** i) * x
    fullsum += linesum
print(fullsum)
index = 0

print("25 Answer 1:", "answer1", "\n25 Answer 2:", "answer2", "\n")
