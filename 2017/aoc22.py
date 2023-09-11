""" 2017 aoc22 """
with open("input22.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

# input_list = "..#\n" \
#              "#..\n" \
#              "...".splitlines()

infected = set()

for x, line in enumerate(input_list):
    for y, char in enumerate(line):
        if char == "#":
            infected.add((x, y))

virus = (len(input_list) // 2, len(input_list[0]) // 2)
facing = "UP"
answer1 = 0
for _ in range(10000):
    if virus in infected:
        infected.remove(virus)
        match facing:
            case "UP":
                facing = "RIGHT"
                virus = (virus[0], virus[1] + 1)
            case "RIGHT":
                facing = "DOWN"
                virus = (virus[0] + 1, virus[1])
            case "DOWN":
                facing = "LEFT"
                virus = (virus[0], virus[1] - 1)
            case "LEFT":
                facing = "UP"
                virus = (virus[0] - 1, virus[1])
    else:
        infected.add(virus)
        answer1 += 1
        match facing:
            case "UP":
                facing = "LEFT"
                virus = (virus[0], virus[1] - 1)
            case "RIGHT":
                facing = "UP"
                virus = (virus[0] - 1, virus[1])
            case "DOWN":
                facing = "RIGHT"
                virus = (virus[0], virus[1] + 1)
            case "LEFT":
                facing = "DOWN"
                virus = (virus[0] + 1, virus[1])

    # for x in range(-10,10):
    #     for y in range(-10,10):
    #         if (x,y) in infected:
    #             print(" # ",end="")
    #         else:
    #             print(" . ",end="")
    #     print()
    # print("----------------------------------------")

print("Answer 1:", answer1)

infected = set()
for x, line in enumerate(input_list):
    for y, char in enumerate(line):
        if char == "#":
            infected.add((x, y))

virus = (len(input_list) // 2, len(input_list[0]) // 2)
facing = "UP"
weakened = set()
flagged = set()
answer2 = 0
for _ in range(10000000):
    if virus in infected:
        infected.remove(virus)
        flagged.add(virus)
        match facing:
            case "UP":
                facing = "RIGHT"
                virus = (virus[0], virus[1] + 1)
            case "RIGHT":
                facing = "DOWN"
                virus = (virus[0] + 1, virus[1])
            case "DOWN":
                facing = "LEFT"
                virus = (virus[0], virus[1] - 1)
            case "LEFT":
                facing = "UP"
                virus = (virus[0] - 1, virus[1])
    elif virus in weakened:
        weakened.remove(virus)
        infected.add(virus)
        answer2 += 1
        match facing:
            case "UP":
                virus = (virus[0] - 1, virus[1])
            case "RIGHT":
                virus = (virus[0], virus[1] + 1)
            case "DOWN":
                virus = (virus[0] + 1, virus[1])
            case "LEFT":
                virus = (virus[0], virus[1] - 1)
    elif virus in flagged:
        flagged.remove(virus)
        match facing:
            case "UP":
                facing = "DOWN"
                virus = (virus[0] + 1, virus[1])
            case "RIGHT":
                facing = "LEFT"
                virus = (virus[0], virus[1] - 1)
            case "DOWN":
                facing = "UP"
                virus = (virus[0] - 1, virus[1])
            case "LEFT":
                facing = "RIGHT"
                virus = (virus[0], virus[1] + 1)
    else:
        weakened.add(virus)
        match facing:
            case "UP":
                facing = "LEFT"
                virus = (virus[0], virus[1] - 1)
            case "RIGHT":
                facing = "UP"
                virus = (virus[0] - 1, virus[1])
            case "DOWN":
                facing = "RIGHT"
                virus = (virus[0], virus[1] + 1)
            case "LEFT":
                facing = "DOWN"
                virus = (virus[0] + 1, virus[1])

print("Answer 2:", answer2)
