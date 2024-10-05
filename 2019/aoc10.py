""" 2019 aoc10 """

with open("input10.txt", "r", encoding="utf-8") as f:
    input_list = [list(x) for x in f.read().splitlines()]


def los(y1, x1, y2, x2):
    x_d, y_d = x1 - x2, y1 - y2
    # print("start", y1, x1)
    # print("goal", y2, x2)
    # print("delta", y_d, x_d)
    if x_d == 0:
        for _i in range(min(y1, y2) + 1, max(y1, y2)):
            if input_list[_i][x1] == "#":
                # print("FALSE")
                # print("##################")
                return False, -1
        # print("TRUE")
        # print("##################")
        if y_d < 0:
            return True, 999
        if y_d > 0:
            return True, 999
    if y_d == 0:
        for _i in range(min(x1, x2) + 1, max(x1, x2)):
            if input_list[y1][_i] == "#":
                # print("FALSE")
                # print("##################")
                return False, -1
        # print("TRUE")
        # print("##################")
        if x_d < 0:
            return True, 0
        if x_d > 0:
            return True, 0
    gcd = 0
    for _i in range(2, min(abs(x_d), abs(y_d)) + 1):
        if x_d % _i == 0 and y_d % _i == 0:
            gcd = _i
    if gcd == 0:
        return True, abs(y_d / x_d)
    x3, y3 = x2, y2
    while (x3 + x_d // gcd) != x1 and (y3 + y_d // gcd) != y1:
        x3 += x_d // gcd
        y3 += y_d // gcd
        if input_list[y3][x3] == "#":
            return False, -1
    return True, abs(y_d / x_d)


max_los = 0
base = (0, 0)
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "#":
            cur_los = 0
            for k, line2 in enumerate(input_list):
                for l, char2 in enumerate(line2):
                    if char2 == "#" and (i != k or j != l):
                        if los(i, j, k, l)[0]:
                            cur_los += 1
            if max_los < cur_los:
                max_los = cur_los
                base = (i, j)

print("Answer 1:", max_los)

gradients1 = {}
gradients2 = {}
gradients3 = {}
gradients4 = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        if char == "#" and (i != base[0] or j != base[1]):
            if los(base[0], base[1], i, j)[0]:
                if i >= base[0]:
                    if j >= base[1]:
                        gradients2[(i, j)] = los(base[0], base[1], i, j)[1]
                    if j < base[1]:
                        gradients3[(i, j)] = los(base[0], base[1], i, j)[1]
                if i < base[0]:
                    if j >= base[1]:
                        gradients1[(i, j)] = los(base[0], base[1], i, j)[1]
                    if j < base[1]:
                        gradients4[(i, j)] = los(base[0], base[1], i, j)[1]

sorted_gradients1 = sorted(gradients1.items(), key=lambda kv: kv[1], reverse=True)
sorted_gradients2 = sorted(gradients2.items(), key=lambda kv: kv[1], reverse=False)
sorted_gradients3 = sorted(gradients3.items(), key=lambda kv: kv[1], reverse=True)
sorted_gradients4 = sorted(gradients4.items(), key=lambda kv: kv[1], reverse=False)
ood = [x[0] for x in sorted_gradients1]
ood = ood + [x[0] for x in sorted_gradients2]
ood = ood + [x[0] for x in sorted_gradients3]
ood = ood + [x[0] for x in sorted_gradients4]
print("Answer 2:", str(ood[199][1]) + "0" + str(ood[199][0]))
