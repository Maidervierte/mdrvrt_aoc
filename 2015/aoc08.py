""" 2015 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    literals = f.read().splitlines()

code = 0
memory = 0
new_enc = 0
for literal in literals:
    new_enc += 6
    code += len(literal)
    i = 1
    while i < len(literal) - 1:
        if literal[i] == "\\":
            if literal[i + 1] == "x":
                memory += 1
                i += 4
                new_enc += 5
            else:
                memory += 1
                i += 2
                new_enc += 4
        else:
            memory += 1
            i += 1
            new_enc += 1
print("Answer 1: " + str(code - memory))
print("Answer 2: " + str(new_enc - code))
