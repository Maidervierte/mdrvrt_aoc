""" 2022 aoc23 """
with open("input23.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

elves = set()
for i1, x in enumerate(input_list):
    for i2, y in enumerate(x):
        if y == "#":
            elves.add((i1, i2))

check = [((-1, 0), (-1, 1), (-1, -1)), ((1, 0), (1, 1), (1, -1)), ((0, -1), (-1, -1), (1, -1),),
         ((0, 1), (-1, 1), (1, 1),)]


def check_move(check_i, elf):
    """check move"""
    returns, moveable = False, []
    for i in range(4):
        adds = True
        for check_offset in check[check_i]:
            if (elf[0] + check_offset[0], elf[1] + check_offset[1]) in elves:
                returns = True
                adds = False
                break
        if adds:
            moveable.append(check[check_i])
        check_i = check_i + 1
        if check_i == 4:
            check_i = 0
    if returns and len(moveable) != 0:
        return moveable[0]
    else:
        return False


check_start, check_i, answer2 = 0, 0, 0

while True:
    temp_set = elves.copy()
    moves = {}
    check_i = check_start
    check_start = check_start + 1
    if check_start == 4:
        check_start = 0
    for elf in sorted(elves):
        checked_move = check_move(check_i, elf)
        if checked_move != False:
            moves[elf] = (elf[0] + checked_move[0][0], elf[1] + checked_move[0][1])
    for key, value in moves.items():
        if list(moves.values()).count(value) > 1:
            continue
        else:
            elves.remove(key)
            elves.add(value)
    if temp_set == elves:
        break
    answer2 += 1
    if answer2 == 9:
        min_x, max_x, min_y, max_y = 999, 0, 999, 0
        for (y, x) in elves:
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
        answer1 = 0
        for x in range(min_y, max_y + 1):
            for y in range(min_x, max_x + 1):
                if (x, y) not in elves: answer1 += 1
print("Answer 1:", answer1)
print("Answer 2:", answer2 + 1)
