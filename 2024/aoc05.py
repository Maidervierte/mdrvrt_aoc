""" 2024 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
rules = {}
breakline = input_list.index("")
for line in input_list[:breakline]:
    key, value = line.split("|")
    if int(key) in rules:
        temp = rules[int(key)]
        temp.append(int(value))
        rules[int(key)] = temp
    else:
        rules[int(key)] = [int(value)]

updates = []
for line in input_list[breakline + 1:]:
    updates.append([int(x) for x in line.split(",")])

incorrects = []
for update in updates:
    correct = True
    for page in update:
        if page in rules:
            for rule in rules[page]:
                if rule not in update:
                    continue
                if update.index(page) > update.index(rule):
                    correct = False
                    incorrects.append(update)
                    break
            else:
                continue
            break
    if correct:
        answer1 += update[len(update) // 2]
print("Answer 1:", answer1)

for incorrect in incorrects:
    correct = False
    while not correct:
        correct = True
        for page in incorrect:
            if page in rules:
                for rule in rules[page]:
                    if rule not in incorrect:
                        continue
                    if incorrect.index(page) > incorrect.index(rule):
                        temp_index = incorrect.index(page)
                        incorrect[incorrect.index(rule)] = page
                        incorrect[temp_index] = rule
                        correct = False
                        break
    answer2 += incorrect[len(incorrect) // 2]
print("Answer 2:", answer2)
