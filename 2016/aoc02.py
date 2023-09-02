""" 2016 aoc02 """
with open("input02.txt", "r", encoding="utf-8") as f:
    number_list = f.read().splitlines()

directions = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

numpad = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

numpad2 = [
    [7, "B", "D", 1, 3],
    [8, "C", 4],
    [9],
    [5],
    [6, "A", 2]
]


def add(x, y):
    return (max(min(x[0] + y[0], 1), -1), max(min(x[1] + y[1], 1), -1))


def add2(x, y):
    return (x[0] + y[0], x[1] + y[1])


def button(cur_pos):
    return numpad[cur_pos[0] + 1][cur_pos[1] + 1]


min_y = [-2, -1, 0, 0, -1]
max_y = [2, 1, 0, 0, 1]

cur_pos = (0, 0)
cur_pos2 = (0, 0)
buttons = []
buttons2 = []
for x in number_list:
    for y in x:
        cur_pos = add(cur_pos, directions[y])
        try:
            if add2(cur_pos2, directions[y])[1] < min_y[cur_pos2[0]]:
                continue
            if add2(cur_pos2, directions[y])[1] > max_y[cur_pos2[0]]:
                continue
            if add2(cur_pos2, directions[y])[0] < min_y[cur_pos2[1]]:
                continue
            if add2(cur_pos2, directions[y])[0] > max_y[cur_pos2[1]]:
                continue
            helper = numpad2[add2(cur_pos2, directions[y])[0]][add2(cur_pos2, directions[y])[1]]
            cur_pos2 = add2(cur_pos2, directions[y])
        except:
            pass
    buttons.append(button(cur_pos))
    buttons2.append(numpad2[cur_pos2[0]][cur_pos2[1]])

print("Answer 1: ", end="")
for x in buttons:
    print(x, end="")
print()
print("Answer 2: ", end="")
for x in buttons2:
    print(x, end="")
