""" 2016 aoc25 """
import time

with open("input25.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

a = 0
b = 0
c = 0
d = 0

j = 0
stop = False
while not stop:
    i = 0
    a = j
    clock = 1
    clocks = [1, 0, 1]
    time1 = time.time()
    while i < len(input_lines) and clocks == [1, 0, 1]:
        if time.time() - time1 > 15:
            print("Answer 1:", j)
            stop = True
            break
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
            case "out":
                exec("clocks[clock]=" + ins.split(" ")[1])
                clock *= -1
                i += 1
    j += 1
