""" 2019 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split(",")]

input_list[1] = 12
input_list[2] = 2
i = 0
while i < len(input_list):
    match input_list[i]:
        case 1:
            input_list[input_list[i + 3]] = \
                input_list[input_list[i + 1]] + input_list[input_list[i + 2]]
        case 2:
            input_list[input_list[i + 3]] = \
                input_list[input_list[i + 1]] * input_list[input_list[i + 2]]
        case 99:
            break
    i += 4

print("Answer 1:", input_list[0])

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split(",")]

for noun in range(100):
    for verb in range(100):
        with open("input02.txt", "r", encoding="utf-8") as f:
            input_list = [int(x) for x in f.read().split(",")]
        input_list[1] = noun
        input_list[2] = verb
        i = 0
        while i < len(input_list):
            match input_list[i]:
                case 1:
                    input_list[input_list[i + 3]] = \
                        input_list[input_list[i + 1]] + input_list[input_list[i + 2]]
                case 2:
                    input_list[input_list[i + 3]] = \
                        input_list[input_list[i + 1]] * input_list[input_list[i + 2]]
                case 99:
                    break
            i += 4
        if input_list[0] == 19690720:
            break
    if input_list[0] == 19690720:
        break

print("Answer 2:", 100 * noun + verb)
