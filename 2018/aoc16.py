""" 2018 aoc16 """
with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

# input_list="Before: [3, 2, 1, 1]\n" \
#            "9 2 1 2\n" \
#            "After:  [3, 2, 2, 1]".splitlines()

samples = []
for line in input_list[:3044]:
    if line == "":
        continue
    if line[0] == "B":
        temp = tuple(int(x) for x in line.split("[")[1][:-1].split(", "))
    if line[0].isdigit():
        temp = (temp, tuple(int(x) for x in line.split(" ")))
    if line[0] == "A":
        samples.append((temp[0], temp[1], tuple(int(x) for x in line.split("[")[1][:-1].split(", "))))

answer1 = 0
opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
           "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
pos_op = []
for _ in range(16):
    pos_op.append(set())

regs_in = ["a1", "b1", "c1", "d1"]
regs_out = ["a2", "b2", "c2", "d2"]
for ((a1, b1, c1, d1), (opcode_num, inp1, inp2, out), check) in samples:
    opcode_counter = 0
    # print("#####################")
    # print("check:", check)
    for opcode in opcodes:
        a2, b2, c2, d2 = a1, b1, c1, d1
        match opcode:
            case "addr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "+" + regs_in[inp2])
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "addi":
                exec(regs_out[out] + "=" + regs_in[inp1] + "+" + str(inp2))
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "mulr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "*" + regs_in[inp2])
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "muli":
                exec(regs_out[out] + "=" + regs_in[inp1] + "*" + str(inp2))
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "banr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "&" + regs_in[inp2])
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "bani":
                exec(regs_out[out] + "=" + regs_in[inp1] + "&" + str(inp2))
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "borr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "|" + regs_in[inp2])
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "bori":
                exec(regs_out[out] + "=" + regs_in[inp1] + "|" + str(inp2))
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "setr":
                exec(regs_out[out] + "=" + regs_in[inp1])
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "seti":
                exec(regs_out[out] + "=" + str(inp1))
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "gtir":
                exec(regs_out[out] + "= 1 if " + str(inp1) + ">" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "gtri":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + ">" + str(inp2) + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "gtrr":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + ">" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "eqir":
                exec(regs_out[out] + "= 1 if " + str(inp1) + "==" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "eqri":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + "==" + str(inp2) + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)
            case "eqrr":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + "==" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) == check:
                    opcode_counter += 1
                    # print(opcode, (a2, b2, c2, d2), opcode_counter)
                    pos_op[opcode_num].add(opcode)

    if opcode_counter > 2:
        answer1 += 1

print("Answer 1:", answer1)

for ((a1, b1, c1, d1), (opcode_num, inp1, inp2, out), check) in samples:
    for opcode in opcodes:
        a2, b2, c2, d2 = a1, b1, c1, d1
        match opcode:
            case "addr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "+" + regs_in[inp2])
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "addi":
                exec(regs_out[out] + "=" + regs_in[inp1] + "+" + str(inp2))
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "mulr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "*" + regs_in[inp2])
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "muli":
                exec(regs_out[out] + "=" + regs_in[inp1] + "*" + str(inp2))
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "banr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "&" + regs_in[inp2])
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "bani":
                exec(regs_out[out] + "=" + regs_in[inp1] + "&" + str(inp2))
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "borr":
                exec(regs_out[out] + "=" + regs_in[inp1] + "|" + regs_in[inp2])
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "bori":
                exec(regs_out[out] + "=" + regs_in[inp1] + "|" + str(inp2))
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "setr":
                exec(regs_out[out] + "=" + regs_in[inp1])
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "seti":
                exec(regs_out[out] + "=" + str(inp1))
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "gtir":
                exec(regs_out[out] + "= 1 if " + str(inp1) + ">" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "gtri":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + ">" + str(inp2) + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "gtrr":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + ">" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "eqir":
                exec(regs_out[out] + "= 1 if " + str(inp1) + "==" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "eqri":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + "==" + str(inp2) + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)
            case "eqrr":
                exec(regs_out[out] + "= 1 if " + regs_in[inp1] + "==" + regs_in[inp2] + " else 0")
                if (a2, b2, c2, d2) != check:
                    if opcode in pos_op[opcode_num]:
                        pos_op[opcode_num].remove(opcode)

for _ in range(16):
    for i in range(16):
        if len(pos_op[i]) == 1:
            for j, x in enumerate(pos_op):
                if i != j and list(pos_op[i])[0] in pos_op[j]:
                    pos_op[j].remove(list(pos_op[i])[0])

program = []
for line in input_list[3047:]:
    program.append(tuple(int(x) for x in line.split(" ")))

regs_p = ["a", "b", "c", "d"]
a = 0
b = 0
c = 0
d = 0
for (opcode_num, inp1, inp2, out) in program:
    opcode = list(pos_op[opcode_num])[0]
    match opcode:
        case "addr":
            exec(regs_p[out] + "=" + regs_p[inp1] + "+" + regs_p[inp2])
        case "addi":
            exec(regs_p[out] + "=" + regs_p[inp1] + "+" + str(inp2))
        case "mulr":
            exec(regs_p[out] + "=" + regs_p[inp1] + "*" + regs_p[inp2])
        case "muli":
            exec(regs_p[out] + "=" + regs_p[inp1] + "*" + str(inp2))
        case "banr":
            exec(regs_p[out] + "=" + regs_p[inp1] + "&" + regs_p[inp2])
        case "bani":
            exec(regs_p[out] + "=" + regs_p[inp1] + "&" + str(inp2))
        case "borr":
            exec(regs_p[out] + "=" + regs_p[inp1] + "|" + regs_p[inp2])
        case "bori":
            exec(regs_p[out] + "=" + regs_p[inp1] + "|" + str(inp2))
        case "setr":
            exec(regs_p[out] + "=" + regs_p[inp1])
        case "seti":
            exec(regs_p[out] + "=" + str(inp1))
        case "gtir":
            exec(regs_p[out] + "= 1 if " + str(inp1) + ">" + regs_p[inp2] + " else 0")
        case "gtri":
            exec(regs_p[out] + "= 1 if " + regs_p[inp1] + ">" + str(inp2) + " else 0")
        case "gtrr":
            exec(regs_p[out] + "= 1 if " + regs_p[inp1] + ">" + regs_p[inp2] + " else 0")
        case "eqir":
            exec(regs_p[out] + "= 1 if " + str(inp1) + "==" + regs_p[inp2] + " else 0")
        case "eqri":
            exec(regs_p[out] + "= 1 if " + regs_p[inp1] + "==" + str(inp2) + " else 0")
        case "eqrr":
            exec(regs_p[out] + "= 1 if " + regs_p[inp1] + "==" + regs_p[inp2] + " else 0")

print("Answer 2:", a)
