""" 2022 aoc02 """
with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def result(p1, p2):
    """calcs result"""
    if p1 + p2 in ["AX", "BY", "CZ"]:
        return 3
    if p1 + p2 in ["AY", "BZ", "CX"]:
        return 6
    return 0


score1, score2 = 0, 0
needed = {"X": 0, "Y": 3, "Z": 6}
for line in input_list:
    for y in ["X", "Y", "Z"]:
        if result(line[0], y) == needed[line[-1]]:
            score2 += result(line[0], y) + ord(y) - 87
    score1 += result(line[0], line[-1]) + ord(line[-1]) - 87

print("Answer 1:", score1)
print("Answer 2:", score2)
