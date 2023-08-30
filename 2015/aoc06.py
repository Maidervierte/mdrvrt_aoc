""" 2015 aoc06 """

with open("input06.txt", "r",encoding="utf-8") as f:
    numberlist = f.read().splitlines()


def on(startx, starty, endx, endy, grid):
    """ turns lights on """
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            grid[x][y] = 1
    return grid


def off(startx, starty, endx, endy, grid):
    """ turns lights off """
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            grid[x][y] = 0
    return grid


def toggle(startx, starty, endx, endy, grid):
    """ toggles lights """
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            if grid[x][y] == 1:
                grid[x][y] = 0
            else:
                grid[x][y] = 1
    return grid


def toggle2(startx, starty, endx, endy, grid):
    """ toggles lights for part 2"""
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            grid[x][y] += 2
    return grid


def on2(startx, starty, endx, endy, grid):
    """ turns lights on for part 2"""
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            grid[x][y] += 1
    return grid


def off2(startx, starty, endx, endy, grid):
    """ turns lights off for part 2"""
    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            if grid[x][y] > 0:
                grid[x][y] -= 1
    return grid


lights = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(0)
    lights.append(temp)

lights2 = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(0)
    lights2.append(temp)

for inst in numberlist:
    split_line = inst.split(" ")
    if "toggle" in inst:
        sx = int(split_line[1].split(",")[0])
        sy = int(split_line[1].split(",")[1])
        ex = int(split_line[3].split(",")[0])
        ey = int(split_line[3].split(",")[1])
        lights = toggle(sx, sy, ex, ey, lights)
        lights2 = toggle2(sx, sy, ex, ey, lights2)
    elif "on" in inst:
        sx = int(split_line[2].split(",")[0])
        sy = int(split_line[2].split(",")[1])
        ex = int(split_line[4].split(",")[0])
        ey = int(split_line[4].split(",")[1])
        lights = on(sx, sy, ex, ey, lights)
        lights2 = on2(sx, sy, ex, ey, lights2)
    elif "off" in inst:
        sx = int(split_line[2].split(",")[0])
        sy = int(split_line[2].split(",")[1])
        ex = int(split_line[4].split(",")[0])
        ey = int(split_line[4].split(",")[1])
        lights = off(sx, sy, ex, ey, lights)
        lights2 = off2(sx, sy, ex, ey, lights2)

sum_lights = 0
for light in lights:
    sum_lights += sum(light)

sum_lights2 = 0
for light in lights2:
    sum_lights2 += sum(light)

print("Answer 1:", sum_lights)
print("Answer 2:", sum_lights2)
