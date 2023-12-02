""" 2023 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

games = []
for line in input_list:
    game = line.split(": ")[-1].split("; ")
    rounds = []
    for r in game:
        rounds.append(r.split(", "))
    games.append(rounds)

red = 12
green = 13
blue = 14
game = 1
answer1 = 0
for x in games:
    add = True
    for y in x:
        for z in y:
            if "red" in z:
                if int(z.split(" ")[0]) > red:
                    add = False
                    # print("red",game,add,x)
                    break
            if "green" in z:
                if int(z.split(" ")[0]) > green:
                    add = False
                    # print("green",game,add,x)
                    break
            if "blue" in z:
                if int(z.split(" ")[0]) > blue:
                    add = False
                    # print("blue",game,add,x)
                    break
    if add:
        # print(game,add,x)
        answer1 += game
    game += 1
print("Answer 1:", answer1)

answer2 = 0
for x in games:
    green = 0
    red = 0
    blue = 0
    for y in x:
        for z in y:
            if "red" in z:
                if int(z.split(" ")[0]) > red:
                    red = int(z.split(" ")[0])
            if "green" in z:
                if int(z.split(" ")[0]) > green:
                    green = int(z.split(" ")[0])
            if "blue" in z:
                if int(z.split(" ")[0]) > blue:
                    blue = int(z.split(" ")[0])
    answer2 += green * red * blue
print("Answer 2:", answer2)
