""" 2017 aoc23 """
import math

with open("input23.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

answer1 = 0
index = 0
while 0 <= index < len(input_list):
    line = input_list[index]
    ins = line.split(" ")[0]
    match ins:
        case "set":
            exec(line.split(" ")[1] + "=" + line.split(" ")[2])
            index += 1
        case "add":
            exec(line.split(" ")[1] + "+=" + line.split(" ")[2])
            index += 1
        case "sub":
            exec(line.split(" ")[1] + "-=" + line.split(" ")[2])
            index += 1
        case "mul":
            exec(line.split(" ")[1] + "*=" + line.split(" ")[2])
            answer1 += 1
            index += 1
        case "mod":
            exec(line.split(" ")[1] + "%=" + line.split(" ")[2])
            index += 1
        case "jnz":
            exec("if " + line.split(" ")[1] + "!=0:index+=" + line.split(" ")[2])
            exec("if " + line.split(" ")[1] + "==0:index+=1")
    #index %= len(input_list)

print("Answer 1:",answer1)

h = 1000
for x in range(105700, 122701, 17):
    for y in range(2, math.floor(math.sqrt(x))):
        if x % y == 0:
            h -= 1
            break
print("Answer 2:", 1000 - h)
