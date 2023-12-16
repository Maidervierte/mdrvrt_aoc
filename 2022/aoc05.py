""" 2022 aoc05 """
with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()
stacks, stack_list, stack_list2 = dict(), [], []

for x in input_list:
    if "move" in x: break
    for index, y in enumerate(x):
        if y == "" or y == " " or y == "[" or y == "]" or y == None:
            continue
        if index in stacks:
            temp = stacks[index]
            temp.append(y)
            stacks[index] = temp
        else:
            stacks[index] = [y]
for key, value in sorted(stacks.items()):
    temp, temp2 = [], []
    for letter in value[:-1]:
        temp.append(letter)
        temp2.append(letter)
    stack_list.append(temp)
    stack_list2.append(temp2)
for line in input_list:
    if "move" in line:
        move = line.split(" ")
        start, amount, end = int(move[3]) - 1, int(move[1]), int(move[5]) - 1
        temp = stack_list[start][:amount]
        temp.reverse()
        stack_list[end], stack_list2[end] = temp + stack_list[end], stack_list2[start][:amount] + stack_list2[end]
        del (stack_list[start][0:amount])
        del (stack_list2[start][0:amount])

print("Answer 1: ", end="")
for x in stack_list: print(x[0], end="")
print("\nAnswer 2: ", end="")
for x in stack_list2: print(x[0], end="")
