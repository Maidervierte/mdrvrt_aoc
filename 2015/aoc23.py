""" 2015 aoc23 """

with open("input23.txt", "r", encoding="utf-8") as f:
    instructions = f.read().splitlines()

instructions = [instruction.split(" ") for instruction in instructions]
i = 0
a = 0
b = 0
while True:
    if i >= len(instructions) or i < 0:
        break
    cur_ins, reg = instructions[i][0], instructions[i][1]
    match cur_ins:
        case "hlf":
            exec(reg + "=" + reg + "//2")
            i += 1
        case "tpl":
            exec(reg + "=" + reg + "*3")
            i += 1
        case "inc":
            exec(reg + "=" + reg + "+1")
            i += 1
        case "jmp":
            i += int(reg)
        case "jie":
            exec("if " + reg[:-1] + "%2==0:i=i" + instructions[i][2] + "\nelse:i+=1")
        case "jio":
            exec("if " + reg[:-1] + "==1:i=i" + instructions[i][2] + "\nelse:i+=1")

print("Answer 1:", b)

i = 0
a = 1
b = 0
while True:
    if i >= len(instructions) or i < 0:
        break
    cur_ins, reg = instructions[i][0], instructions[i][1]
    match cur_ins:
        case "hlf":
            exec(reg + "=" + reg + "//2")
            i += 1
        case "tpl":
            exec(reg + "=" + reg + "*3")
            i += 1
        case "inc":
            exec(reg + "=" + reg + "+1")
            i += 1
        case "jmp":
            i += int(reg)
        case "jie":
            exec("if " + reg[:-1] + "%2==0:i=i" + instructions[i][2] + "\nelse:i+=1")
        case "jio":
            exec("if " + reg[:-1] + "==1:i=i" + instructions[i][2] + "\nelse:i+=1")

print("Answer 2:", b)
