""" 2016 aoc08 """
with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

# input_list = ["rect 3x3", "rotate row x=0 by 153", "rotate column y=0 by 1"]
screen = [["⬜" for x in range(50)] for y in range(6)]

for line in input_list:
    line_split = line.split(" ")
    temp_screen = []
    for screen_line in screen:
        temp_screen.append(screen_line)
    if line_split[0] == "rect":
        x = int(line_split[1].split("x")[0])
        y = int(line_split[1].split("x")[1])
        for _x in range(x):
            for _y in range(y):
                screen[_y][_x] = "⬛"
    if line_split[0] == "rotate":
        if line_split[1] == "column":
            column = int(line_split[2].split("=")[1])
            by = int(line_split[-1])
            for i in range(len(screen)):
                temp1 = temp_screen[i][:column]
                temp1.append(temp_screen[i - (by % 6)][column])
                temp2 = temp_screen[i][column + 1:]
                screen[i] = temp1 + temp2
        elif line_split[1] == "row":
            row = int(line_split[2].split("=")[1])
            by = int(line_split[-1])
            screen[row] = screen[row][-(by % 50):] + screen[row][:-(by % 50)]

answer1 = 0
for line in screen:
    answer1 += line.count("⬛")
print("Answer 1:", answer1)
for line in screen:
    print(line)
