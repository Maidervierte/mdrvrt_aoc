""" 2024 aoc11"""

with open("input11.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split(" ")]

answer1 = 0
answer2 = 0
blinks = 75
stones = {}
for line in input_list:
    stones[line] = 1
for blink in range(blinks):
    if blink == 25:
        answer1 += sum(stones.values())
    temp = {}
    for stone, number in stones.items():
        if stone == 0:
            next_stone = 1
            if next_stone in temp:
                temp[next_stone] += number
            else:
                temp[next_stone] = number
        elif len(str(stone)) % 2 == 0:
            next_stone1 = int(str(stone)[:len(str(stone)) // 2])
            next_stone2 = int(str(stone)[len(str(stone)) // 2:])
            if next_stone1 in temp:
                temp[next_stone1] += number
            else:
                temp[next_stone1] = number
            if next_stone2 in temp:
                temp[next_stone2] += number
            else:
                temp[next_stone2] = number
        else:
            next_stone = stone * 2024
            if next_stone in temp:
                temp[next_stone] += number
            else:
                temp[next_stone] = number
    stones = temp
answer2 += sum(stones.values())
print("Answer 1:", answer1)
print("Answer 2:", answer2)
