""" 2016 aoc12 """

with open("input12.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

a = 0
b = 0
c = 0
d = 0

i = 0
while i < len(input_lines):
    ins = input_lines[i]
    match ins.split(" ")[0]:
        case "cpy":
            exec(ins.split(" ")[2] + "=" + ins.split(" ")[1])
            i += 1
        case "inc":
            exec(ins.split(" ")[1] + "+=1")
            i += 1
        case "dec":
            exec(ins.split(" ")[1] + "-=1")
            i += 1
        case "jnz":
            jnz = 0
            exec("jnz=" + ins.split(" ")[1])
            if jnz != 0:
                i += int(ins.split(" ")[2])
            else:
                i += 1

print("Answer 1:", a)

a = 0
b = 0
c = 1
d = 0

i = 0
while i < len(input_lines):
    ins = input_lines[i]
    match ins.split(" ")[0]:
        case "cpy":
            exec(ins.split(" ")[2] + "=" + ins.split(" ")[1])
            i += 1
        case "inc":
            exec(ins.split(" ")[1] + "+=1")
            i += 1
        case "dec":
            exec(ins.split(" ")[1] + "-=1")
            i += 1
        case "jnz":
            jnz = 0
            exec("jnz=" + ins.split(" ")[1])
            if jnz != 0:
                i += int(ins.split(" ")[2])
            else:
                i += 1

print("Answer 2:", a)
