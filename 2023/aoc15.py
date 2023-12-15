""" 2023 aoc15 """

with open("input15.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split(",")

answer1 = 0
for i, line in enumerate(input_list):
    temp = 0
    for char in line:
        temp = ((temp + ord(char)) * 17) % 256
    answer1 += temp
print("Answer 1:", answer1)

boxes = [[] for x in range(256)]
focal_lengths = {}
for i, lens in enumerate(input_list):
    if "-" in lens:
        label = lens[:-1]
        box = 0
        for char in label:
            box = ((box + ord(char)) * 17) % 256
        if label in boxes[box]:
            boxes[box].remove(label)
    else:
        label, focal_length = lens.split("=")[0], int(lens.split("=")[1])
        box = 0
        for char in label:
            box = ((box + ord(char)) * 17) % 256
        if label not in boxes[box]:
            boxes[box].append(label)
        focal_lengths[label, box] = focal_length

answer2 = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        answer2 += (i + 1) * (j + 1) * focal_lengths[lens, i]
print("Answer 2:", answer2)
