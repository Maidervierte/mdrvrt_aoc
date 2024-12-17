""" 2024 aoc17"""

with open("input17.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0

a = int(input_list[0].split(": ")[1])
b = int(input_list[1].split(": ")[1])
c = int(input_list[2].split(": ")[1])
output = []
ins_pointer = 0
program = [int(x) for x in input_list[-1].split(": ")[1].split(",")]
while ins_pointer < len(program):
    opcode = program[ins_pointer]
    operand = program[ins_pointer + 1]
    operands = [0, 1, 2, 3, a, b, c]
    match opcode:
        case 0:  # adv
            a = int(a / (2 ** operands[operand]))
            ins_pointer += 2
        case 1:  # bxl
            b = b ^ operand
            ins_pointer += 2
        case 2:  # bst
            b = operands[operand] % 8
            ins_pointer += 2
        case 3:  # jnz
            if a != 0:
                ins_pointer = operand
            else:
                ins_pointer += 2
        case 4:  # bxc
            b = b ^ c
            ins_pointer += 2
        case 5:  # out
            output.append(operands[operand] % 8)
            ins_pointer += 2
        case 6:  # bdv
            b = int(a / (2 ** operands[operand]))
            ins_pointer += 2
        case 7:  # cdv
            c = int(a / (2 ** operands[operand]))
            ins_pointer += 2
answer1 = ",".join([str(x) for x in output])
print("Answer 1:", answer1)

program = [int(x) for x in input_list[-1].split(": ")[1].split(",")]
start_a = 8 ** 15
while True:
    ins_pointer = 0
    output = []
    a = start_a
    b = int(input_list[1].split(": ")[1])
    c = int(input_list[2].split(": ")[1])
    while ins_pointer < len(program):
        opcode = program[ins_pointer]
        operand = program[ins_pointer + 1]
        operands = [0, 1, 2, 3, a, b, c]
        match opcode:
            case 0:  # adv
                a = int(a / (2 ** operands[operand]))
                ins_pointer += 2
            case 1:  # bxl
                b = b ^ operand
                ins_pointer += 2
            case 2:  # bst
                b = operands[operand] % 8
                ins_pointer += 2
            case 3:  # jnz
                if a != 0:
                    ins_pointer = operand
                else:
                    ins_pointer += 2
            case 4:  # bxc
                b = b ^ c
                ins_pointer += 2
            case 5:  # out
                output.append(operands[operand] % 8)
                ins_pointer += 2
            case 6:  # bdv
                b = int(a / (2 ** operands[operand]))
                ins_pointer += 2
            case 7:  # cdv
                c = int(a / (2 ** operands[operand]))
                ins_pointer += 2
    for j in range(-1, -17, -1):
        if output[j] != program[j]:
            start_a += 8 ** (16 + j)
            break
    if len(output) > len(program):
        break
    if output == program:
        answer2 = start_a
        break

print("Answer 2:", answer2)
