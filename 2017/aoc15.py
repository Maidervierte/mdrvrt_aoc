""" 2017 aoc15 """

with open("input15.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

a = int(input_list[0].split(" ")[-1])
b = int(input_list[1].split(" ")[-1])
answer1 = 0
for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if bin(a)[-16:] == bin(b)[-16:]:
        answer1 += 1
print("Answer 1:", answer1)

a = int(input_list[0].split(" ")[-1])
b = int(input_list[1].split(" ")[-1])
answer2 = 0
for _ in range(5000000):
    a = (a * 16807) % 2147483647
    while int(str(a)[-2:]) % 4 != 0:
        a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while int(str(b)[-3:]) % 8 != 0:
        b = (b * 48271) % 2147483647
    if bin(a)[-16:] == bin(b)[-16:]:
        answer2 += 1
print("Answer 2:", answer2)
