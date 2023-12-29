""" 2023 aoc24 """

with open("input24.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

hail = {}
for i, line in enumerate(input_list):
    line = line.split(" @")
    x, y, z = [int(x) for x in line[0].split(", ")]
    vx, vy, vz = [int(x) for x in line[1].split(", ")]
    hail[i] = ((x, y, z), (vx, vy, vz))

lower = 200000000000000
upper = 400000000000000
answer1 = 0

for i, stone1 in enumerate(list(hail.keys())):
    for stone2 in list(hail.keys())[i:]:
        if stone1 == stone2:
            continue

        ((a, b, _), (va, vb, _)) = hail[stone1]
        ((x, y, _), (vx, vy, _)) = hail[stone2]

        m1 = vb / va
        b1 = -m1 * a + b

        m2 = vy / vx
        b2 = -m2 * x + y

        if m1 == m2:
            continue

        x0 = (-b2 + b1) / (-m1 + m2)
        y0 = (b1 * m2 - b2 * m1) / (-m1 + m2)

        if not lower <= x0 <= upper:
            continue

        if not lower <= y0 <= upper:
            continue

        if (va > 0 and x0 < a) or (va < 0 and x0 > a):
            continue
        if (vx > 0 and x0 < x) or (vx < 0 and x0 > x):
            continue
        if (vb > 0 and y0 < b) or (vb < 0 and y0 > b):
            continue
        if (vy > 0 and y0 < y) or (vy < 0 and y0 > y):
            continue
        answer1 += 1
print("Answer 1:", answer1)

collision = False
for svx in range(-1000, 1000):
    if collision:
        collision = False
        break
    for svy in range(-1000, 1000):
        col_x = []
        col_y = []
        stone1 = 0
        ((a1, b1, _), (va1, vb1, _)) = hail[stone1]
        va1 -= svx
        vb1 -= svy
        for stone2 in list(hail)[1:]:
            ((a2, b2, _), (va2, vb2, _)) = hail[stone2]
            va2 -= svx
            vb2 -= svy

            try:
                m1 = vb1 / va1
                q1 = -m1 * a1 + b1

                m2 = vb2 / va2
                q2 = -m2 * a2 + b2
            except:
                continue

            if m1 == m2:
                # print("m1==m2")
                collision = False
                break

            x0 = (-q2 + q1) / (-m1 + m2)
            y0 = (q1 * m2 - q2 * m1) / (-m1 + m2)

            if (va1 > 0 and x0 < a1) or (va1 < 0 and x0 > a1):
                # print("past x1:", x0)
                collision = False
                break
            if (va2 > 0 and x0 < a2) or (va2 < 0 and x0 > a2):
                # print("past x2", x0)
                collision = False
                break
            if (vb1 > 0 and y0 < b1) or (vb1 < 0 and y0 > b1):
                # print("past y1", y0)
                collision = False
                break
            if (vb2 > 0 and y0 < b2) or (vb2 < 0 and y0 > b2):
                # print("past y2", y0)
                collision = False
                break
            col_x.append(x0)
            col_y.append(y0)
            x0 = round(x0)
            y0 = round(y0)
            x0 = int(str(x0)[:-3])
            y0 = int(str(y0)[:-3])
            # print(x0,y0)
            if not collision:
                collision = (x0, y0)
            elif (x0, y0) != collision:
                collision = False
                break
        if collision:
            x0 = col_x[0]
            for x in col_x[1:]:
                x0 += x
                x0 /= 2
            y0 = col_y[0]
            for x in col_y[1:]:
                y0 += x
                y0 /= 2
            break

collision = False
for svz in range(-1000, 1000):
    col_y = []
    col_z = []
    stone1 = len(hail) - 1
    ((_, a1, b1), (_, va1, vb1)) = hail[stone1]
    va1 -= svy
    vb1 -= svz
    for stone2 in list(hail)[:-1]:
        ((_, a2, b2), (_, va2, vb2)) = hail[stone2]
        va2 -= svy
        vb2 -= svz

        try:
            m1 = vb1 / va1
            q1 = -m1 * a1 + b1

            m2 = vb2 / va2
            q2 = -m2 * a2 + b2
        except:
            continue

        if m1 == m2:
            # print("m1==m2")
            collision = False
            break

        y0 = (-q2 + q1) / (-m1 + m2)
        z0 = (q1 * m2 - q2 * m1) / (-m1 + m2)

        if (va1 > 0 and y0 < a1) or (va1 < 0 and y0 > a1):
            # print("past x1:", x0)
            collision = False
            break
        if (va2 > 0 and y0 < a2) or (va2 < 0 and y0 > a2):
            # print("past x2", x0)
            collision = False
            break
        if (vb1 > 0 and z0 < b1) or (vb1 < 0 and z0 > b1):
            # print("past y1", y0)
            collision = False
            break
        if (vb2 > 0 and z0 < b2) or (vb2 < 0 and z0 > b2):
            # print("past y2", y0)
            collision = False
            break
        col_y.append(y0)
        col_z.append(z0)
        y0 = round(y0)
        z0 = round(z0)
        y0 = int(str(y0)[:-3])
        z0 = int(str(z0)[:-3])
        if not collision:
            collision = (y0, z0)
        elif (y0, z0) != collision:
            collision = False
            break
    if collision:
        y0 = col_y[0]
        for x in col_y[1:]:
            y0 += x
            y0 /= 2
        z0 = col_z[0]
        for x in col_z[1:]:
            z0 += x
            z0 /= 2
        print("Answer 2:", round(x0) + round(y0) + round(z0))
        break
