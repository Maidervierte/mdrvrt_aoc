""" 2017 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

# input_lines = "b inc 5 if a > 1\n" \
#               "a inc 1 if b < 5\n" \
#               "c dec -10 if a >= 1\n" \
#               "c inc -20 if c == 10".splitlines()

for line in input_lines:
    var1, _, _, _, var2, _, _ = line.split(" ")
    exec(var1 + "=0")
    exec(var2 + "=0")

max_val = 0
for line in input_lines:
    var1, ins, val1, _, var2, comp, val2 = line.split(" ")
    if ins == "inc":
        exec("if " + var2 + comp + val2 + ": " + var1 + "+=" + val1)
    else:
        exec("if " + var2 + comp + val2 + ": " + var1 + "-=" + val1)
    registers = []
    exec("max_val=max(max_val," + var1 + ")")

registers = []
for line in input_lines:
    var1, _, _, _, var2, _, _ = line.split(" ")
    exec("registers.append(" + var1 + ")")
    exec("registers.append(" + var2 + ")")

print("Answer 1:", max(registers))
print("Answer 2:", max_val)
