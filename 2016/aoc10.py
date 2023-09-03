""" 2016 aoc10 """

with open("input10.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

bots = [[] for _ in range(210)]
output = [0 for _ in range(21)]

for line in input_lines:
    line_split = line.split(" ")
    if line_split[0] == "value":
        bots[int(line_split[-1])].append(int(line_split[1]))
    if line_split[0] == "bot":
        pass

input_lines = [[int(x) if x.isdigit() else x for x in y.split(" ")]
               for y in input_lines if y.split(" ")[0] != "value"]
input_lines = sorted(input_lines, key=lambda x: x[1])

iterations = 0
while iterations < 1000:
    for i, bot in enumerate(bots):
        if len(bot) == 2:
            _, _, _, _, _, _low, low, _, _, _, _high, high = input_lines[i]
            if _low == "output":
                output[int(low)] = (min(bots[i]))
            else:
                bots[int(low)].append(min(bots[i]))
            if _high == "output":
                output[int(high)] = (max(bots[i]))
            else:
                bots[int(high)].append(max(bots[i]))
            if (max(bot), min(bot)) == (61, 17):
                print("Answer 1:", i)
            bots[i] = []
            break
    iterations += 1

print("Answer 2:", output[0] * output[1] * output[2])
