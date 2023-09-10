""" 2017 aoc03 """

with open("input03.txt", "r", encoding="utf-8") as f:
    input_number = int(f.read())

count = 1
pos = (0, 0)
do = 1
steps = 1
inc = False
while count != input_number:
    match do:
        case 1:
            do += 1
            for _ in range(steps):
                count += 1
                pos = (pos[0] + 1, pos[1])
                if count >= input_number:
                    break
        case 2:
            do += 1
            for _ in range(steps):
                count += 1
                pos = (pos[0], pos[1] + 1)
                if count >= input_number:
                    break
        case 3:
            do += 1
            for _ in range(steps):
                count += 1
                pos = (pos[0] - 1, pos[1])
                if count >= input_number:
                    break
        case 4:
            do = 1
            for _ in range(steps):
                count += 1
                pos = (pos[0], pos[1] - 1)
                if count >= input_number:
                    break
    if inc:
        steps += 1
        inc = False
    else:
        inc = True
print("Answer 1:", abs(pos[0]) + abs(pos[1]))

pos = (0, 0)
do = 1
steps = 1
inc = False
squares = {}
squares[(0, 0)] = 1
cur_value = 1
while cur_value <= input_number:
    match do:
        case 1:
            do += 1
            for _ in range(steps):
                pos = (pos[0] + 1, pos[1])
                cur_value = 0
                for x in range(pos[0] - 1, pos[0] + 2):
                    for y in range(pos[1] - 1, pos[1] + 2):
                        if (x, y) in squares:
                            cur_value += squares[(x, y)]
                squares[pos] = cur_value
                if cur_value > input_number:
                    break
        case 2:
            do += 1
            for _ in range(steps):
                count += 1
                pos = (pos[0], pos[1] + 1)
                cur_value = 0
                for x in range(pos[0] - 1, pos[0] + 2):
                    for y in range(pos[1] - 1, pos[1] + 2):
                        if (x, y) in squares:
                            cur_value += squares[(x, y)]
                squares[pos] = cur_value
                if cur_value > input_number:
                    break
        case 3:
            do += 1
            for _ in range(steps):
                count += 1
                pos = (pos[0] - 1, pos[1])
                cur_value = 0
                for x in range(pos[0] - 1, pos[0] + 2):
                    for y in range(pos[1] - 1, pos[1] + 2):
                        if (x, y) in squares:
                            cur_value += squares[(x, y)]
                squares[pos] = cur_value
                if cur_value > input_number:
                    break
        case 4:
            do = 1
            for _ in range(steps):
                count += 1
                pos = (pos[0], pos[1] - 1)
                cur_value = 0
                for x in range(pos[0] - 1, pos[0] + 2):
                    for y in range(pos[1] - 1, pos[1] + 2):
                        if (x, y) in squares:
                            cur_value += squares[(x, y)]
                squares[pos] = cur_value
                if cur_value > input_number:
                    break
    if inc:
        steps += 1
        inc = False
    else:
        inc = True
print("Answer 2:", cur_value)
