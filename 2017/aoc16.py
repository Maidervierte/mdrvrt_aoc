""" 2017 aoc16 """

with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split(",")

programs = [chr(x) for x in range(97, 113)]
for line in input_list:
    match line[0]:
        case "s":
            num = int(line[1:])
            programs = programs[-num:] + programs[:16 - num]
        case "x":
            i1 = int(line[1:].split("/")[0])
            i2 = int(line[1:].split("/")[1])
            p1 = programs[i1]
            programs[i1] = programs[i2]
            programs[i2] = p1
        case "p":
            p1 = line[1]
            p2 = line[3]
            i1 = programs.index(p1)
            i2 = programs.index(p2)
            programs[i1] = p2
            programs[i2] = p1
print("Answer 1:", "".join(programs))

programs = [chr(x) for x in range(97, 113)]
i = 1
while i < 1000000001:
    for line in input_list:
        match line[0]:
            case "s":
                num = int(line[1:])
                programs = programs[-num:] + programs[:16 - num]
            case "x":
                i1 = int(line[1:].split("/")[0])
                i2 = int(line[1:].split("/")[1])
                p1 = programs[i1]
                programs[i1] = programs[i2]
                programs[i2] = p1
            case "p":
                p1 = line[1]
                p2 = line[3]
                i1 = programs.index(p1)
                i2 = programs.index(p2)
                programs[i1] = p2
                programs[i2] = p1
    if programs == [chr(x) for x in range(97, 113)]:
        mult = 1000000000 // i
        i = mult * i
    i += 1
print("Answer 2:", "".join(programs))
