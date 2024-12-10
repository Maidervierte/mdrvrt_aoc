""" 2020 aoc14 """

with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = [x.strip() for x in f.read().split("mask = ")][1:]

mask_list = []
for line in input_list:
    temp = []
    for item in [x.strip() for x in line.split("mem[")]:
        temp.append([int(x) if x.isdigit() else x for x in item.split("] = ")])
    mask_list.append(temp)

memory = {}
for initialization in mask_list:
    mask = initialization[0][0]
    operations = initialization[1:]
    for operation in operations:
        # print("----------------------------------------------")
        bin_val = bin(operation[1])
        # print("0" * (len(mask) - len(bin_val[2:])) + bin_val[2:])
        # print(mask)
        result = ""
        for i, bit in enumerate(reversed(bin_val[2:])):
            # print(str(i)+":", bit, mask[-i])
            if mask[-i - 1] != "X":
                result = mask[-i - 1] + result
            else:
                result = str(bit) + result
        result = "".join([x if x == "1" else "0" for x in mask[:-len(result)]]) + result
        # print(mask)
        # print(result, int(result, 2))
        memory[operation[0]] = int(result, 2)
answer1 = sum(memory.values())
print("Answer 1:", answer1)

memory = {}
for initialization in mask_list:
    mask = initialization[0][0]
    operations = initialization[1:]
    for operation in operations:
        bin_add = bin(operation[0])
        base_address = ""
        for i, bit in enumerate(reversed(bin_add[2:])):
            if mask[-i - 1] != "0":
                base_address = mask[-i - 1] + base_address
            else:
                base_address = str(bit) + base_address
        base_address = mask[:-len(base_address)] + base_address
        addresses = [base_address]
        temp = addresses
        while temp:
            addresses = temp
            temp = []
            for address in addresses:
                if "X" not in address:
                    continue
                temp_add = address
                temp_add = temp_add[:address.index("X")] + "1" + temp_add[address.index("X") + 1:]
                temp.append(temp_add)
                temp_add = temp_add[:address.index("X")] + "0" + temp_add[address.index("X") + 1:]
                temp.append(temp_add)
        for address in addresses:
            memory[int(address, 2)] = operation[1]
answer2 = sum(memory.values())
print("Answer 2:", answer2)
