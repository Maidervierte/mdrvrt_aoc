""" 2023 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

games = []
for line in input_list:
    game = [r.split(", ") for r in line.split(": ")[-1].split("; ")]
    games.append(game)

red, green, blue = 12, 13, 14
game = 1
answer1 = 0
for x in games:
    add = True
    for y in x:
        for z in y:
            if "red" in z and int(z.split(" ")[0]) > red:
                add = False
                break
            if "green" in z and int(z.split(" ")[0]) > green:
                add = False
                break
            if "blue" in z and int(z.split(" ")[0]) > blue:
                add = False
                break

    if add:
        answer1 += game
    game += 1
print("Answer 1:", answer1)

answer2 = 0
for x in games:
    green, red, blue = 0, 0, 0
    for y in x:
        for z in y:
            if "red" in z and int(z.split(" ")[0]) > red:
                red = int(z.split(" ")[0])
            if "green" in z and int(z.split(" ")[0]) > green:
                green = int(z.split(" ")[0])
            if "blue" in z and int(z.split(" ")[0]) > blue:
                blue = int(z.split(" ")[0])
    answer2 += green * red * blue
print("Answer 2:", answer2)
