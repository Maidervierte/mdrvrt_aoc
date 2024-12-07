""" 2020 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = [x.split(" ") for x in f.read().splitlines()]

acc = 0
i = 0
ins_counter = [0 for x in range(len(input_list))]
ins_counter[0] = 1
while sorted(ins_counter)[-1] < 2:
    ins, val = input_list[i][0], int(input_list[i][1])
    match ins:
        case "acc":
            acc += val
            i += 1
        case "jmp":
            i += val
        case "nop":
            i += 1
    ins_counter[i] += 1
answer1 = acc
print("Answer 1:", answer1)

for j, _ in enumerate(input_list):
    if input_list[j][0] == "jmp":
        input_list[j][0] = "nop"
    elif input_list[j][0] == "nop":
        input_list[j][0] = "jmp"
    else:
        continue
    acc = 0
    i = 0
    ins_counter = [0 for x in range(len(input_list))]
    ins_counter[0] = 1
    while sorted(ins_counter)[-1] < 2 and i < len(input_list):
        ins, val = input_list[i][0], int(input_list[i][1])
        match ins:
            case "acc":
                acc += val
                i += 1
            case "jmp":
                i += val
            case "nop":
                i += 1
        if i < len(ins_counter):
            ins_counter[i] += 1
    if input_list[j][0] == "jmp":
        input_list[j][0] = "nop"
    elif input_list[j][0] == "nop":
        input_list[j][0] = "jmp"
    if i >= len(input_list):
        answer2 = acc
        print("Answer 2:", answer2)
