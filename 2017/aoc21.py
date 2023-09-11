""" 2017 aoc21 """
with open("input21.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

start = ".#.\n" \
        "..#\n" \
        "###".splitlines()

patterns = {}
for line in input_list:
    line_split = line.split(" => ")
    orig_pattern = [list(x) for x in line_split[0].split("/")]
    from_patterns = []
    to_pattern = line_split[1].split("/")
    if len(orig_pattern) == 2:
        from_patterns.append([[orig_pattern[0][0], orig_pattern[0][1]],
                              [orig_pattern[1][0], orig_pattern[1][1]]])

        from_patterns.append([[orig_pattern[0][1], orig_pattern[0][0]],
                              [orig_pattern[1][1], orig_pattern[1][0]]])

        from_patterns.append([[orig_pattern[1][1], orig_pattern[1][0]],
                              [orig_pattern[0][1], orig_pattern[0][0]]])

        from_patterns.append([[orig_pattern[1][0], orig_pattern[1][1]],
                              [orig_pattern[0][0], orig_pattern[0][1]]])

        from_patterns.append([[orig_pattern[0][0], orig_pattern[1][0]],
                              [orig_pattern[0][1], orig_pattern[1][1]]])

        from_patterns.append([[orig_pattern[1][0], orig_pattern[0][0]],
                              [orig_pattern[1][1], orig_pattern[0][1]]])
    else:
        from_patterns.append([[orig_pattern[0][0], orig_pattern[0][1], orig_pattern[0][2]],
                              [orig_pattern[1][0], orig_pattern[1][1], orig_pattern[1][2]],
                              [orig_pattern[2][0], orig_pattern[2][1], orig_pattern[2][2]]])

        from_patterns.append([[orig_pattern[2][0], orig_pattern[1][0], orig_pattern[0][0]],
                              [orig_pattern[2][1], orig_pattern[1][1], orig_pattern[0][1]],
                              [orig_pattern[2][2], orig_pattern[1][2], orig_pattern[0][2]]])

        from_patterns.append([[orig_pattern[2][2], orig_pattern[2][1], orig_pattern[2][0]],
                              [orig_pattern[1][2], orig_pattern[1][1], orig_pattern[1][0]],
                              [orig_pattern[0][2], orig_pattern[0][1], orig_pattern[0][0]]])

        from_patterns.append([[orig_pattern[0][2], orig_pattern[1][2], orig_pattern[2][2]],
                              [orig_pattern[0][1], orig_pattern[1][1], orig_pattern[2][1]],
                              [orig_pattern[0][0], orig_pattern[1][0], orig_pattern[2][0]]])

        from_patterns.append([[orig_pattern[0][2], orig_pattern[0][1], orig_pattern[0][0]],
                              [orig_pattern[1][2], orig_pattern[1][1], orig_pattern[1][0]],
                              [orig_pattern[2][2], orig_pattern[2][1], orig_pattern[2][0]]])

        from_patterns.append([[orig_pattern[0][0], orig_pattern[1][0], orig_pattern[2][0]],
                              [orig_pattern[0][1], orig_pattern[1][1], orig_pattern[2][1]],
                              [orig_pattern[0][2], orig_pattern[1][2], orig_pattern[2][2]]])

        from_patterns.append([[orig_pattern[2][0], orig_pattern[2][1], orig_pattern[2][2]],
                              [orig_pattern[1][0], orig_pattern[1][1], orig_pattern[1][2]],
                              [orig_pattern[0][0], orig_pattern[0][1], orig_pattern[0][2]]])

        from_patterns.append([[orig_pattern[2][2], orig_pattern[1][2], orig_pattern[0][2]],
                              [orig_pattern[2][1], orig_pattern[1][1], orig_pattern[0][1]],
                              [orig_pattern[2][0], orig_pattern[1][0], orig_pattern[0][0]]])
    for from_pattern in from_patterns:
        patterns[tuple(tuple(x) for x in from_pattern)] = to_pattern

# for pattern in patterns.keys():
#     for line in pattern:
#         print(line)
#     print()

cur_artwork = [list(x) for x in start]
for iteration in range(18):
    if len(cur_artwork) % 2 == 0:
        new_artwork = [["" for x in range((len(cur_artwork) // 2) * 3)] for y in range((len(cur_artwork) // 2) * 3)]
        for x in range(0, len(cur_artwork), 2):
            for y in range(0, len(cur_artwork), 2):
                cur_pattern = ((cur_artwork[x][y], cur_artwork[x][y + 1]),
                               (cur_artwork[x + 1][y], cur_artwork[x + 1][y + 1]))
                new_pattern = patterns[cur_pattern]
                a = (x // 2) * 3
                b = (y // 2) * 3
                for c in range(3):
                    for d in range(3):
                        new_artwork[a + c][b + d] = new_pattern[c][d]
    else:
        new_artwork = [["" for x in range((len(cur_artwork) // 3) * 4)] for y in range((len(cur_artwork) // 3) * 4)]
        for x in range(0, len(cur_artwork), 3):
            for y in range(0, len(cur_artwork), 3):
                cur_pattern = ((cur_artwork[x][y], cur_artwork[x][y + 1], cur_artwork[x][y + 2]),
                               (cur_artwork[x + 1][y], cur_artwork[x + 1][y + 1], cur_artwork[x + 1][y + 2]),
                               (cur_artwork[x + 2][y], cur_artwork[x + 2][y + 1], cur_artwork[x + 2][y + 2]))
                new_pattern = patterns[cur_pattern]
                a = (x // 3) * 4
                b = (y // 3) * 4
                for c in range(4):
                    for d in range(4):
                        new_artwork[a + c][b + d] = new_pattern[c][d]
    cur_artwork = []
    for line in new_artwork:
        cur_artwork.append(line)
    if iteration==4:
        answer1 = 0
        for x in cur_artwork:
            answer1 += x.count("#")
        print("Answer 1:", answer1)

answer2 = 0
for x in cur_artwork:
    answer2 += x.count("#")
print("Answer 2:", answer2)
