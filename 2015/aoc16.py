""" 2015 aoc16 """
with open("input16.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

sues = {}
sue0 = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}

for line in input_lines:
    _, sue, thing1, amount1, thing2, amount2, thing3, amount3 = line.split(" ")
    sues[int(sue[:-1])] = {}
    sues[int(sue[:-1])][thing1[:-1]] = int(amount1[:-1])
    sues[int(sue[:-1])][thing2[:-1]] = int(amount2[:-1])
    sues[int(sue[:-1])][thing3[:-1]] = int(amount3)

for sue, values in sues.items():
    skip=False
    for thing, amount in values.items():
        if sue0[thing]!=amount:
            skip=True
            break
    if skip:
        continue
    print("Answer 1:",sue)
    break

pos_sues=[]
for sue, values in sues.items():
    skip=False
    for thing, amount in values.items():
        if thing=="cats" or thing=="trees":
            if amount<=sue0[thing]:
                skip=True
                break
        elif thing=="pomeranians" or thing=="goldfish":
            if amount>=sue0[thing]:
                skip=True
                break
        elif sue0[thing]!=amount:
            skip=True
            break
    if skip:
        continue
    print("Answer 2:",sue)
