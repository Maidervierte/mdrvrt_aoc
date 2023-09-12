""" 2018 aoc12 """
with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

initial_state = input_list[0].split("initial state: ")[1]

input_list = input_list[2:]

rules = {}
for line in input_list:
    rules[line.split(" => ")[0]] = line.split(" => ")[1]

pots = {}
for i, char in enumerate(initial_state):
    pots[i] = char

generations = 20
for _ in range(generations):
    new_pots = pots.copy()
    for pot_index in range(min(pots.keys()) - 2, max(pots.keys()) + 3):
        cur_pots = ""
        for i in range(pot_index - 2, pot_index + 3):
            if i in pots:
                cur_pots += pots[i]
            else:
                cur_pots += "."
        new_pots[pot_index] = rules[cur_pots]
    pots = new_pots.copy()

answer1 = 0
for key, value in pots.items():
    if value == "#":
        answer1 += key
print("Answer 1:", answer1)

pots = {}
for i, char in enumerate(initial_state):
    pots[i] = char

answer2 = 0
generations = 1000
for gen in range(generations):
    new_pots = pots.copy()
    for pot_index in range(min(pots.keys()) - 2, max(pots.keys()) + 3):
        cur_pots = ""
        for i in range(pot_index - 2, pot_index + 3):
            if i in pots:
                cur_pots += pots[i]
            else:
                cur_pots += "."
        new_pots[pot_index] = rules.get(cur_pots)
    pots = new_pots.copy()
for key, value in pots.items():
    if value == "#":
        answer2 += key
print("Answer 2:", answer2 + ((50000000000 - generations) * 5))
