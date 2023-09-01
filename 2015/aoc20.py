""" 2015 aoc20 """
import math  # for square root

with open("input20.txt", "r", encoding="utf-8") as f:
    input_number = int(f.read())

presents_sum = 0
house = 1
while presents_sum < input_number:
    presents = set()
    for elf in range(1, (math.floor(math.sqrt(house))) + 1):
        if house % elf == 0:
            presents.add(elf)
            presents.add(house // elf)
    presents_sum = sum(presents) * 10
    house += 1
print("Answer 1:", house - 1)

presents_sum = 0
house = 1
while presents_sum < input_number:
    presents = set()
    for elf in range(1, (math.floor(math.sqrt(house))) + 1):
        if house % elf == 0:
            if elf * 50 >= house:
                presents.add(elf)
            if (house // elf) * 50 >= house:
                presents.add(house // elf)
    presents_sum = sum(presents) * 11
    house += 1
print("Answer 2:", house - 1)
