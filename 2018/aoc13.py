""" 2018 aoc13 """
with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

with open("input13_2.txt", "r", encoding="utf-8") as f:
    clean_input = f.read().splitlines()

grid = {}
mine_carts = {}
next_tile = (0, 0)

for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char != " ":
            grid[(i, j)] = char
        if char in ["<", ">", "v", "^"]:
            mine_carts[(i, j)] = (char, "LEFT")

answer1 = True
directions = ["LEFT", "STRAIGHT", "RIGHT"]
while len(mine_carts) > 1:
    new_carts = {}
    for x in range(len(input_list)):
        for y in range(len(input_list[0]) * 4):
            if (x, y) in mine_carts:
                cart, direction = mine_carts[(x, y)]
                match cart:
                    case "<":
                        next_tile = (x, y - 1)
                        if grid[next_tile] in ["<", ">", "v", "^"]:
                            if answer1:
                                print("Answer 1:", str(next_tile[1]) + "," + str(next_tile[0]))
                                answer1 = False
                            grid[(x, y)] = clean_input[x][y]
                            grid[next_tile] = clean_input[next_tile[0]][next_tile[1]]
                            if next_tile in mine_carts:
                                mine_carts.pop(next_tile)
                            else:
                                new_carts.pop(next_tile)
                            break
                        match grid[next_tile]:
                            case "+":
                                dir_i = directions.index(direction)
                                match dir_i:
                                    case 0:
                                        new_carts[next_tile] = ("v", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 1:
                                        new_carts[next_tile] = ("<", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 2:
                                        new_carts[next_tile] = ("^", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                            case "/":
                                new_carts[next_tile] = ("v", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case "\\":
                                new_carts[next_tile] = ("^", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case _:
                                new_carts[next_tile] = (cart, direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                    case ">":
                        next_tile = (x, y + 1)
                        if grid[next_tile] in ["<", ">", "v", "^"]:
                            if answer1:
                                print("Answer 1:", str(next_tile[1]) + "," + str(next_tile[0]))
                                answer1 = False
                            grid[(x, y)] = clean_input[x][y]
                            grid[next_tile] = clean_input[next_tile[0]][next_tile[1]]
                            if next_tile in mine_carts:
                                mine_carts.pop(next_tile)
                            else:
                                new_carts.pop(next_tile)
                            break
                        match grid[next_tile]:
                            case "+":
                                dir_i = directions.index(direction)
                                match dir_i:
                                    case 0:
                                        new_carts[next_tile] = ("^", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 1:
                                        new_carts[next_tile] = (">", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 2:
                                        new_carts[next_tile] = ("v", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                            case "/":
                                new_carts[next_tile] = ("^", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case "\\":
                                new_carts[next_tile] = ("v", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case _:
                                new_carts[next_tile] = (cart, direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                    case "^":
                        next_tile = (x - 1, y)
                        if grid[next_tile] in ["<", ">", "v", "^"]:
                            if answer1:
                                print("Answer 1:", str(next_tile[1]) + "," + str(next_tile[0]))
                                answer1 = False
                            grid[(x, y)] = clean_input[x][y]
                            grid[next_tile] = clean_input[next_tile[0]][next_tile[1]]
                            if next_tile in mine_carts:
                                mine_carts.pop(next_tile)
                            else:
                                new_carts.pop(next_tile)
                            break
                        match grid[next_tile]:
                            case "+":
                                dir_i = directions.index(direction)
                                match dir_i:
                                    case 0:
                                        new_carts[next_tile] = ("<", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 1:
                                        new_carts[next_tile] = ("^", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 2:
                                        new_carts[next_tile] = (">", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                            case "/":
                                new_carts[next_tile] = (">", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case "\\":
                                new_carts[next_tile] = ("<", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case _:
                                new_carts[next_tile] = (cart, direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                    case "v":
                        next_tile = (x + 1, y)
                        if grid[next_tile] in ["<", ">", "v", "^"]:
                            if answer1:
                                print("Answer 1:", str(next_tile[1]) + "," + str(next_tile[0]))
                                answer1 = False
                            grid[(x, y)] = clean_input[x][y]
                            grid[next_tile] = clean_input[next_tile[0]][next_tile[1]]
                            if next_tile in mine_carts:
                                mine_carts.pop(next_tile)
                            else:
                                new_carts.pop(next_tile)
                            break
                        match grid[next_tile]:
                            case "+":
                                dir_i = directions.index(direction)
                                match dir_i:
                                    case 0:
                                        new_carts[next_tile] = (">", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 1:
                                        new_carts[next_tile] = ("v", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                                    case 2:
                                        new_carts[next_tile] = ("<", directions[(dir_i + 1) % 3])
                                        grid[(x, y)] = clean_input[x][y]
                                        grid[next_tile] = new_carts[next_tile][0]
                            case "/":
                                new_carts[next_tile] = ("<", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case "\\":
                                new_carts[next_tile] = (">", direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
                            case _:
                                new_carts[next_tile] = (cart, direction)
                                grid[(x, y)] = clean_input[x][y]
                                grid[next_tile] = new_carts[next_tile][0]
    mine_carts = new_carts.copy()
    # for x in range(len(input_list)):
    #     for y in range(len(input_list[0])*4):
    #         if (x,y) in grid:
    #             print(grid[x,y],end="")
    #         else:
    #             print(" ",end="")
    #     print()
    # print()

for (x,y) in mine_carts.keys():
    print("Answer 2:",str(y)+","+str(x))
