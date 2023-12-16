""" 2022 aoc09 """
with open("input09.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def check_tail(head, tail):
    distance = (abs(tail[0] - head[0]) + abs(tail[1] - head[1]))
    if distance < 2:
        return tail
    if tail[0] == head[0] and tail[1] < head[1]:
        return (tail[0], tail[1] + 1)
    if tail[0] == head[0] and tail[1] > head[1]:
        return (tail[0], tail[1] - 1)
    if tail[1] == head[1] and tail[0] < head[0]:
        return (tail[0] + 1, tail[1])
    if tail[1] == head[1] and tail[0] > head[0]:
        return (tail[0] - 1, tail[1])
    if distance == 2:
        return tail
    if tail[1] < head[1] and tail[0] < head[0]:
        return (tail[0] + 1, tail[1] + 1)
    if tail[1] < head[1] and tail[0] > head[0]:
        return (tail[0] - 1, tail[1] + 1)
    if tail[1] > head[1] and tail[0] < head[0]:
        return (tail[0] + 1, tail[1] - 1)
    if tail[1] > head[1] and tail[0] > head[0]:
        return (tail[0] - 1, tail[1] - 1)


knots = [(0, 0)] * 10
visited, visited2 = set(), set()
for line in input_list:
    direction, steps = line.split()
    for index in range(int(steps)):
        if direction == "U":
            knots[0] = (knots[0][0] - 1, knots[0][1])
        if direction == "R":
            knots[0] = (knots[0][0], knots[0][1] + 1)
        if direction == "D":
            knots[0] = (knots[0][0] + 1, knots[0][1])
        if direction == "L":
            knots[0] = (knots[0][0], knots[0][1] - 1)
        for i1 in range(1, 10):
            knots[i1] = check_tail(knots[i1 - 1], knots[i1])
        visited.add(knots[1])
        visited2.add(knots[-1])

print("Answer 1:", len(visited))
print("Answer 2:", len(visited2))
