""" 2022 aoc10 """
with open("input10.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()
signal = [1]
for line in input_list:
    if "noop" in line:
        signal.append(signal[-1])
    else:
        signal += [signal[-1], signal[-1] + int(line.split()[1])]

print("Answer 1:", (
    sum([signal[19] * 20, signal[59] * 60, signal[99] * 100, signal[139] * 140, signal[179] * 180, signal[219] * 220])))

for y in range(6):
    for x in range(40):
        if signal[0] - 1 <= x <= signal[0] + 1:
            print("⬛", end="")
        else:
            print("⬜", end="")
        signal.pop(0)
    print()
