""" 2022 aoc11 """
with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

monkeys, temp = [], []
for line in input_list:
    if "Monkey" in line:
        monkeys.append(temp)
        temp = [int(line.split()[1][:-1])]
    elif "items" in line:
        temp.append([line.split(", ")[0][-2:]] + line.split(", ")[1:])
        temp.append([line.split(", ")[0][-2:]] + line.split(", ")[1:])
    elif "Operation" in line:
        temp.append(line.split()[4:6])
    elif "Test" in line:
        temp.append(int(line.split()[-1]))
    elif "true" in line:
        temp.append(int(line.split()[-1]))
    elif "false" in line:
        temp.append(int(line.split()[-1]))

monkeys.append(temp)
monkeys = monkeys[1:]

for monkey in monkeys:
    monkey.append(0)
    monkey.append(0)

for rounds in range(10000):
    for monkey in monkeys:
        while len(monkey[1]) > 0 and rounds < 20:
            monkey[-1] += 1
            old = monkey[1][0]
            old = int(old) % 9699690
            if monkey[3][1] == "old" and monkey[3][0] == "*":
                new = old * old
            elif monkey[3][1] == "old" and monkey[3][0] == "+":
                new = old + old
            elif monkey[3][1] != "old" and monkey[3][0] == "*":
                new = old * int(monkey[3][1])
            elif monkey[3][1] != "old" and monkey[3][0] == "+":
                new = old + int(monkey[3][1])
            new2 = new // 3
            if (new2 % monkey[4]) == 0:
                monkeys[monkey[5]][1].append(new2)
            else:
                monkeys[monkey[6]][1].append(new2)
            monkey[1].pop(0)
        while len(monkey[2]) > 0:
            monkey[-2] += 1
            old = monkey[2][0]
            old = int(old) % 9699690
            if monkey[3][1] == "old" and monkey[3][0] == "*":
                new = old * old
            elif monkey[3][1] == "old" and monkey[3][0] == "+":
                new = old + old
            elif monkey[3][1] != "old" and monkey[3][0] == "*":
                new = old * int(monkey[3][1])
            elif monkey[3][1] != "old" and monkey[3][0] == "+":
                new = old + int(monkey[3][1])
            if (new % monkey[4]) == 0:
                monkeys[monkey[5]][2].append(new)
            else:
                monkeys[monkey[6]][2].append(new)
            monkey[2].pop(0)

highest1, highest2 = [], []
for monkey in monkeys:
    highest1.append(monkey[-1])
    highest2.append(monkey[-2])

print("Answer 1:", sorted((highest1))[-1] * sorted((highest1))[-2])
print("Answer 2:", sorted((highest2))[-1] * sorted((highest2))[-2])
