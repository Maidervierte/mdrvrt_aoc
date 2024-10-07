""" 2019 aoc16 """

with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read()]

base = [0, 1, 0, -1]

cur_signal = input_list.copy()
for phase in range(10):
    output = []
    for i in range(len(cur_signal)):
        new_digit = 0
        for j, digit in enumerate(cur_signal):
            new_digit += digit * base[((j + 1) // (i + 1)) % 4]
        output.append(int(str(new_digit)[-1]))
    cur_signal = output.copy()

print("Answer 1:", "".join([str(x) for x in cur_signal[:8]]))

real_input_list = input_list * 10000
needed_input_list = real_input_list[int("".join([str(x) for x in real_input_list[:7]])):]
cur_signal = needed_input_list.copy()

for phase in range(100):
    output = [sum(cur_signal) % 10]
    for i in range(1, len(cur_signal)):
        output.append((output[i - 1] - cur_signal[i - 1]) % 10)
    cur_signal = output.copy()
print("Answer 2:", "".join([str(x) for x in cur_signal[:8]]))
