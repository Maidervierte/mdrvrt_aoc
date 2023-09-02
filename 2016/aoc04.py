""" 2016 aoc04 """
from collections import Counter

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

room_list = []
for x in input_list:
    room_list.append(x.replace("[", "-").replace("]", "-").split("-")[:-1])

sec_sum = 0
for x in room_list:
    c = Counter()
    for y in range(len(x) - 2):
        c += Counter(x[y])
    j = 0
    temp = 0
    temp_key = ""
    top5 = ""
    for key in reversed(sorted(c, key=c.get)):
        if temp != c[key]:
            top5 += "".join(sorted(temp_key))
            temp_key = ""
        temp_key += key
        temp = c[key]
    top5 += "".join(sorted(temp_key))
    top5 = top5[:5]
    if top5 == x[-1]:
        sec_sum += int(x[-2])
    new_string = ""
    for y in x[:-2]:
        for z in y:
            letter = z
            for a in range(int(x[-2])):
                letter = chr(ord(letter) + 1)
                if ord(letter) == 123:
                    letter = "A"
                if ord(letter) == 91:
                    letter = "a"
            new_string += letter
        new_string += " "
    if new_string.lower().strip() == "northpole object storage":
        answer2 = x[-2]
print("Answer 1:", sec_sum)
print("Answer 2:", answer2)
