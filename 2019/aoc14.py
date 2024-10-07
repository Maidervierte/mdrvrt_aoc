""" 2019 aoc14 """

with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = [[[(int(z.split(" ")[0]), z.split(" ")[1]) for z in y.split(", ")] for y in x.split(" => ")] for x in
                  f.read().splitlines()]

storage = {}
needed = {"FUEL": 1}
answer1 = 0

while needed:
    for key, value in list(needed.items()):
        for line in input_list:
            if line[1][0][1] == key:
                if key in storage:
                    storage[key] += line[1][0][0]
                else:
                    storage[key] = line[1][0][0]
                for chemical in line[0]:
                    if chemical[1] in needed:
                        needed[chemical[1]] += chemical[0]
                    else:
                        needed[chemical[1]] = chemical[0]
    for key, value in list(storage.items()):
        if key in needed:
            if storage[key] < needed[key]:
                needed[key] -= storage[key]
                storage.pop(key)
            elif storage[key] == needed[key]:
                storage.pop(key)
                needed.pop(key)
            elif storage[key] > needed[key]:
                storage[key] -= needed[key]
                needed.pop(key)
    if "ORE" in needed:
        answer1 += needed.pop("ORE")

storage = {}
ore = 0
fuel = 0
while ore < 1000000000000:
    needed = {"FUEL": 1}
    fuel += 1
    while needed:
        for key, value in list(needed.items()):
            for line in input_list:
                if line[1][0][1] == key:
                    if key in storage:
                        storage[key] += line[1][0][0]
                    else:
                        storage[key] = line[1][0][0]
                    for chemical in line[0]:
                        if chemical[1] in needed:
                            needed[chemical[1]] += chemical[0]
                        else:
                            needed[chemical[1]] = chemical[0]
        for key, value in list(storage.items()):
            if key in needed:
                if storage[key] < needed[key]:
                    needed[key] -= storage[key]
                    storage.pop(key)
                elif storage[key] == needed[key]:
                    storage.pop(key)
                    needed.pop(key)
                elif storage[key] > needed[key]:
                    storage[key] -= needed[key]
                    needed.pop(key)
        if "ORE" in needed:
            ore += needed.pop("ORE")

print("Answer 1:", answer1)
print("Answer 2:", fuel)
