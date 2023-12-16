""" 2022 aoc20 """
with open("input20.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def mix(indices, new_list):
    """mix"""
    for key1, value1 in sorted(mix_order.items()):
        old_index = indices[key1]
        new_index = old_index + key1[1]
        if new_index >= len(input_list):
            new_index %= len(input_list) - 1
        if new_index < 0:
            temp = (-new_index) // (len(input_list) - 1)
            new_index = new_index + (temp + 1) * (len(input_list) - 1)
            if new_index == (len(input_list) - 1):
                new_index = 0
        if new_index == 0:
            new_index = len(input_list) - 1
        indices[key1] = new_index
        if new_index < old_index:
            for key2, value2 in indices.items():
                if new_index <= value2 <= old_index and key1 != key2:
                    indices[key2] += 1
        if new_index > old_index:
            for key2, value2 in indices.items():
                if new_index >= value2 > old_index and key1 != key2:
                    indices[key2] -= 1
    for key2, value2 in indices.items():
        new_list[value2] = key2[1]
    return new_list


def answer(new_list, zero_index):
    """answer"""
    coords = []
    for x in range(1000, 4000, 1000):
        coord_index = zero_index + x
        if coord_index >= len(new_list):
            coord_index = coord_index % len(new_list)
        coords.append(new_list[coord_index])
    return coords


input_list = [int(line) for line in input_list]
indices = {}

for index, x in enumerate(input_list):
    indices[(index, x)] = index

new_list, mix_order = input_list.copy(), indices.copy()
new_list = mix(indices, new_list)
zero_index = new_list.index(0)
answer1 = sum(answer(new_list, zero_index))
decryption_key = 811589153
indices = {}
input_list = [x * decryption_key for x in input_list]

for index, x in enumerate(input_list):
    indices[(index, x)] = index
new_list, mix_order = input_list.copy(), indices.copy()

for iterations in range(10):
    new_list = mix(indices, new_list)

zero_index = new_list.index(0)
answer2 = sum(answer(new_list, zero_index))
print("Answer 1:", answer1)
print("Answer 2:", answer2)
