""" 2019 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    intput_list = [int(x) for x in f.read().split(",")]


def intcode(program, intcode_input, part, debug):
    """runs intcode program"""
    i = 0
    while i < len(program):
        mode1 = 0
        mode2 = 0
        mode3 = 0
        opcode = str(program[i])
        if debug:
            print("position", i, "is", opcode)
        if len(opcode) > 2:
            mode1 = int(opcode[-3])
            if len(opcode) > 3:
                mode2 = int(opcode[-4])
            if len(opcode) > 4:
                mode3 = int(opcode[-5])
            opcode = int(opcode[-2:])
        else:
            opcode = int(opcode)
        match opcode:
            case 1:  # addition
                if debug:
                    print("add:")
                match mode1:
                    case 0:
                        add1 = program[program[i + 1]]
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                    case 1:
                        add1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                match mode2:
                    case 0:
                        add2 = program[program[i + 2]]
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                    case 1:
                        add2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                program[program[i + 3]] = add1 + add2
                if debug:
                    print("  ", program[i + 3], "is", add1 + add2)
                i += 4
            case 2:
                if debug:
                    print("mult:")
                match mode1:
                    case 0:
                        mult1 = program[program[i + 1]]
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                    case 1:
                        mult1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                match mode2:
                    case 0:
                        mult2 = program[program[i + 2]]
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                    case 1:
                        mult2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                program[program[i + 3]] = mult1 * mult2
                if debug:
                    print("  ", program[i + 3], "is", mult1 + mult2)
                i += 4
            case 3:
                if debug:
                    print("input:")
                program[program[i + 1]] = intcode_input
                if debug:
                    print("  position", program[i + 1], "is", intcode_input)
                i += 2
            case 4:
                if debug:
                    print("output")
                match mode1:
                    case 0:
                        intcode_output = program[program[i + 1]]
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                    case 1:
                        intcode_output = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                if intcode_output != 0:
                    if debug:
                        print("   intcode_output is", intcode_output)
                    print("Answer " + str(part) + ":", intcode_output)
                else:
                    if debug:
                        print("   no output")
                i += 2
            case 5:
                if debug:
                    print("jump if not 0")
                match mode1:
                    case 0:
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                        par1 = program[program[i + 1]]
                    case 1:
                        par1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                match mode2:
                    case 0:
                        par2 = program[program[i + 2]]
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                    case 1:
                        par2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                if par1 != 0:
                    if debug:
                        print("   jump to", par2)
                    i = par2
                else:
                    if debug:
                        print("   no jump")
                    i += 3
            case 6:
                if debug:
                    print("jump if 0")
                match mode1:
                    case 0:
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                        par1 = program[program[i + 1]]
                    case 1:
                        par1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                match mode2:
                    case 0:
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                        par2 = program[program[i + 2]]
                    case 1:
                        par2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                if par1 == 0:
                    if debug:
                        print("   jump to", par2)
                    i = par2
                else:
                    if debug:
                        print("   no jump")
                    i += 3
            case 7:
                if debug:
                    print("less than")
                match mode1:
                    case 0:
                        par1 = program[program[i + 1]]
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                    case 1:
                        par1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 2])
                match mode2:
                    case 0:
                        par2 = program[program[i + 2]]
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                    case 1:
                        par2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                if par1 < par2:
                    program[program[i + 3]] = 1
                    if debug:
                        print(par1, par2, "less than true")
                        print("   position", program[i + 3], "is", 1)
                else:
                    program[program[i + 3]] = 0
                    if debug:
                        print(par1, par2, "less than false")
                        print("   position", program[i + 3], "is", 0)
                i += 4
            case 8:
                if debug:
                    print("equals")
                match mode1:
                    case 0:
                        par1 = program[program[i + 1]]
                        if debug:
                            print("   position", program[i + 1], "is", program[program[i + 1]])
                    case 1:
                        par1 = program[i + 1]
                        if debug:
                            print("   immediate", program[i + 1])
                match mode2:
                    case 0:
                        par2 = program[program[i + 2]]
                        if debug:
                            print("   position", program[i + 2], "is", program[program[i + 2]])
                    case 1:
                        par2 = program[i + 2]
                        if debug:
                            print("   immediate", program[i + 2])
                if par1 == par2:
                    program[program[i + 3]] = 1
                    if debug:
                        print(par1, par2, "equals true")
                        print("   position", program[i + 3], "is", 1)
                else:
                    program[program[i + 3]] = 0
                    if debug:
                        print(par1, par2, "equals false")
                        print("   position", program[i + 3], "is", 0)
                i += 4
            case 99:
                if debug:
                    print("   fin")
                break
        if debug:
            print()


intcode(intput_list.copy(), 1, 1, False)
intcode(intput_list.copy(), 5, 2, False)
