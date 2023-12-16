""" 2022 aoc13 """
with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

temp = []
for line in input_list:
    if line != "":
        temp.append(eval(line.strip()))
input_list = temp


def comp_list(item1, item2, padd):
    """comps... list"""
    for index, x in enumerate(item1):
        if index == len(item2):
            return False
        if type(item1[index]) == int and type(item2[index]) == int:
            if item1[index] == item2[index]:
                continue
            if int(item1[index]) < int(item2[index]):
                return True
            else:
                return False
        if type(item1[index]) == list and type(item2[index]) == list:
            if len(x) == 0 and len(item2[index]) == 0: continue
            padd += "-"
            try:
                if comp_list(item1[index], item2[index], padd):
                    return True
                return False
            except:
                continue
        if type(item1[index]) == list and type(item2[index]) == int:
            padd += "-"
            try:
                if comp_list(item1[index], [item2[index]], padd):
                    return True
                return False
            except:
                continue
        if type(item1[index]) == int and type(item2[index]) == list:
            padd += "-"
            try:
                if comp_list([item1[index]], item2[index], padd):
                    return True
                return False
            except:
                continue
    if str(item1) == str(item2):
        raise Exception("continue")
    return True


counter = 0
lines = []
for line in range(0, len(input_list) - 1, 2):
    item1 = input_list[line]
    item2 = input_list[line + 1]
    padd = "-"
    cur_ans = comp_list(item1, item2, padd)
    if cur_ans:
        lines.append((line // 2) + 1)
        counter += (line // 2) + 1

input_list.append([[2]])
input_list.append([[6]])
for iteration1 in range(len(input_list)):
    for iteration2 in range(len(input_list) - 1):
        if comp_list(input_list[iteration2], input_list[iteration2 + 1], "-"):
            continue
        else:
            temp = input_list[iteration2]
            input_list[iteration2] = input_list[iteration2 + 1]
            input_list[iteration2 + 1] = temp
for index, line in enumerate(input_list):
    if str(line) == "[[2]]":
        div1 = index + 1
    if str(line) == "[[6]]":
        div2 = index + 1

print("Answer 1:", counter)
print("Answer 2:", div1 * div2)
