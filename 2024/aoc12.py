""" 2024 aoc12"""

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
garden = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        garden[i, j] = char

visited = set()
for (i, j), plant in garden.items():
    if (i, j) in visited:
        continue
    plot = set()
    temp = set()
    temp.add((i, j))
    visited.add((i, j))
    while temp != plot:
        plot = set(temp)
        for _i, _j in plot:
            for x, y in [(_i + 1, _j), (_i, _j + 1), (_i - 1, _j), (_i, _j - 1)]:
                if (x, y) in garden and garden[x, y] == plant:
                    temp.add((x, y))
                    visited.add((x, y))
    plot_perimeter = 0
    for _i, _j in plot:
        for x, y in [(_i + 1, _j), (_i, _j + 1), (_i - 1, _j), (_i, _j - 1)]:
            if (x, y) not in garden or garden[x, y] != plant:
                plot_perimeter += 1
    answer1 += len(plot) * plot_perimeter

print("Answer 1:", answer1)

garden = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        for x in range(3):
            for y in range(3):
                garden[i * 3 + x, j * 3 + y] = char

visited = set()
for (i, j), plant in garden.items():
    if (i, j) in visited:
        continue
    plot = set()
    temp = set()
    temp.add((i, j))
    visited.add((i, j))
    while temp != plot:
        plot = set(temp)
        for _i, _j in plot:
            for x, y in [(_i + 1, _j), (_i, _j + 1), (_i - 1, _j), (_i, _j - 1)]:
                if (x, y) in garden and garden[x, y] == plant:
                    temp.add((x, y))
                    visited.add((x, y))
    plot_perimeter = set()
    for _i, _j in plot:
        for x, y in [(_i + 1, _j), (_i, _j + 1),
                     (_i + 1, _j + 1), (_i - 1, _j + 1),
                     (_i - 1, _j), (_i, _j - 1),
                     (_i - 1, _j - 1), (_i + 1, _j - 1)]:
            if (x, y) not in garden or (x, y) not in plot:
                plot_perimeter.add((x, y))
    plot_sides = 0
    perimeter_visited = set()
    for _x, _y in plot_perimeter:
        if (_x, _y) in perimeter_visited:
            continue
        plot_sides += 1
        plot_side = set()
        temp = set()
        temp.add((_x, _y))
        perimeter_visited.add((_x, _y))
        while temp != plot_side:
            plot_side = set(temp)
            for _i, _j in plot_side:
                for x, y in [(_i + 1, _j), (_i - 1, _j)]:
                    if (x, y) in plot_perimeter:
                        temp.add((x, y))
                        perimeter_visited.add((x, y))
        if len(plot_side) == 1:
            perimeter_visited.remove((_x, _y))
            plot_sides -= 1
    perimeter_visited = set()
    for _x, _y in plot_perimeter:
        if (_x, _y) in perimeter_visited:
            continue
        plot_sides += 1
        plot_side = set()
        temp = set()
        temp.add((_x, _y))
        perimeter_visited.add((_x, _y))
        while temp != plot_side:
            plot_side = set(temp)
            for _i, _j in plot_side:
                for x, y in [(_i, _j + 1), (_i, _j - 1)]:
                    if (x, y) in plot_perimeter:
                        temp.add((x, y))
                        perimeter_visited.add((x, y))
        if len(plot_side) == 1:
            perimeter_visited.remove((_x, _y))
            plot_sides -= 1
    answer2 += len(plot)//9 * plot_sides
print("Answer 2:", answer2)
