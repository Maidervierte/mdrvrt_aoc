""" 2022 aoc12 """
with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

for i1, line in enumerate(input_list):
    if "S" in line:
        start = (i1, line.index("S"))
    if "E" in line:
        end = (i1, line.index("E"))


def task(inputs):
    """task"""
    start, inputlist, end, = inputs[0], inputs[1], inputs[2]
    reachable, first = {start: 0}, True,
    while end not in reachable:
        temp = reachable.copy()
        for (x, y), distance in reachable.items():
            if first and inputlist[x][y] == "a": first_a, first = distance, False
            if x != 0 and (x - 1, y) not in temp and (ord(inputlist[x - 1][y]) >= (ord(inputlist[x][y]) - 1)): temp[
                (x - 1, y)] = distance + 1
            if x != len(inputlist) - 1 and (x + 1, y) not in temp and (
                    ord(inputlist[x + 1][y]) >= (ord(inputlist[x][y]) - 1)): temp[(x + 1, y)] = distance + 1
            if y != 0 and (x, y - 1) not in temp and (ord(inputlist[x][y - 1]) >= (ord(inputlist[x][y]) - 1)): temp[
                (x, y - 1)] = distance + 1
            if y != len(inputlist[0]) - 1 and (x, y + 1) not in temp and (
                    ord(inputlist[x][y + 1]) >= (ord(inputlist[x][y]) - 1)): temp[(x, y + 1)] = distance + 1
        if len(reachable) == len(temp): return -1
        reachable = temp.copy()
    return (reachable[end], first_a)


input_list[start[0]] = input_list[start[0]][:start[1]] + "a" + input_list[start[0]][start[1] + 1:]
input_list[end[0]] = input_list[end[0]][:end[1]] + "z" + input_list[end[0]][end[1] + 1:]
answers = task([end, input_list, start])
print("Answer 1:", answers[0])
print("Answer 2:", answers[1])
