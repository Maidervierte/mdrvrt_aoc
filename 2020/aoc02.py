""" 2020 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = [x.split(": ") for x in f.read().splitlines()]

answer1 = 0
answer2 = 0
for line in input_list:
    min_letter, max_letter, letter = int(line[0].split("-")[0]), int(line[0].split("-")[1][:-2]), line[0].split(" ")[1]
    if min_letter <= line[1].count(letter) <= max_letter:
        answer1 += 1
    if (line[1][min_letter - 1] == letter) ^ (line[1][max_letter - 1] == letter):
        answer2 += 1
print("Answer 1:", answer1)
print("Answer 2:", answer2)
