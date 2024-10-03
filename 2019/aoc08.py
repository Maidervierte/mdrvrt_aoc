""" 2019 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in list(f.read())]

x = 25
y = 6
image = []
k = 0
while True:
    layer = []
    for i in range(y):
        line = []
        for j in range(x):
            line.append(input_list[k * x * y + i * x + j])
        layer.append(line)
    image.append(layer)
    if k * x * y + i * x + j + 1 == len(input_list):
        break
    k += 1

target_layer = -1
min_z = x * y + 1

for i, layer in enumerate(image):
    z_count = 0
    for line in layer:
        z_count += line.count(0)
    if z_count < min_z:
        min_z = z_count
        target_layer = i

count_1 = 0
count_2 = 0
for line in image[target_layer]:
    count_1 += line.count(1)
    count_2 += line.count(2)

print("Answer 1:", count_1 * count_2)

answer2 = []
for i in range(y):
    line = []
    for j in range(x):
        for k in range(len(input_list) // (x * y)):
            if image[k][i][j] == 1:
                line.append("⬜")
                break
            if image[k][i][j] == 0:
                line.append("⬛")
                break
    answer2.append(line)

print("Answer 2:")
for line in answer2:
    print(line)
