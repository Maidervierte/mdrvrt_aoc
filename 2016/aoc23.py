""" 2016 aoc23 """
with open("input23.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

a = 7
b = 0
c = 0
d = 0

i = 0
while i < len(input_lines):
    ins = input_lines[i]
    match ins.split(" ")[0]:
        case "cpy":
            try:
                exec(ins.split(" ")[2] + "=" + ins.split(" ")[1])
            except:
                pass
            i += 1
        case "inc":
            try:
                exec(ins.split(" ")[1] + "+=1")
            except:
                pass
            i += 1
        case "dec":
            try:
                exec(ins.split(" ")[1] + "-=1")
            except:
                pass
            i += 1
        case "jnz":
            jnz = 0
            try:
                exec("jnz=" + ins.split(" ")[1])
                if jnz != 0:
                    exec("i+=" + ins.split(" ")[2])
                else:
                    i += 1
            except:
                i += 1
        case "tgl":
            tgl = i
            exec("tgl+=" + ins.split(" ")[1])
            tgl %= len(input_lines)
            match input_lines[tgl].split(" ")[0]:
                case "inc":
                    input_lines[tgl] = "dec " + " ".join(input_lines[tgl].split(" ")[1:])
                case "tgl":
                    input_lines[tgl] = "inc " + " ".join(input_lines[tgl].split(" ")[1:])
                case "dec":
                    input_lines[tgl] = "inc " + " ".join(input_lines[tgl].split(" ")[1:])
                case "jnz":
                    input_lines[tgl] = "cpy " + " ".join(input_lines[tgl].split(" ")[1:])
                case "cpy":
                    input_lines[tgl] = "jnz " + " ".join(input_lines[tgl].split(" ")[1:])
            i += 1

print("Answer 1:", a)

with open("input23.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

a = 12
b = 0
c = 0
d = 0

i = 0
while i < len(input_lines):
    ins = input_lines[i]
    if i == 2:
        a = a * b
        b -= 1
        i = 11
        continue
    match ins.split(" ")[0]:
        case "cpy":
            try:
                exec(ins.split(" ")[2] + "=" + ins.split(" ")[1])
            except:
                pass
            i += 1
        case "inc":
            try:
                exec(ins.split(" ")[1] + "+=1")
            except:
                pass
            i += 1
        case "dec":
            try:
                exec(ins.split(" ")[1] + "-=1")
            except:
                pass
            i += 1
        case "jnz":
            jnz = 0
            try:
                exec("jnz=" + ins.split(" ")[1])
                if jnz != 0:
                    exec("i+=" + ins.split(" ")[2])
                else:
                    i += 1
            except:
                i += 1
        case "tgl":
            tgl = i
            exec("tgl+=" + ins.split(" ")[1])
            if -1 < tgl < len(input_lines):
                match input_lines[tgl].split(" ")[0]:
                    case "inc":
                        input_lines[tgl] = "dec " + " ".join(input_lines[tgl].split(" ")[1:])
                    case "tgl":
                        input_lines[tgl] = "inc " + " ".join(input_lines[tgl].split(" ")[1:])
                    case "dec":
                        input_lines[tgl] = "inc " + " ".join(input_lines[tgl].split(" ")[1:])
                    case "jnz":
                        input_lines[tgl] = "cpy " + " ".join(input_lines[tgl].split(" ")[1:])
                    case "cpy":
                        input_lines[tgl] = "jnz " + " ".join(input_lines[tgl].split(" ")[1:])
            i += 1

print("Answer 2:", a)
