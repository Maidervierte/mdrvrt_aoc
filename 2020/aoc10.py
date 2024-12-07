""" 2020 aoc10 """

with open("input10.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().splitlines()]

input_list = sorted(input_list)
cur_j = 0
joltdiff = {0: 0, 1: 0, 2: 0, 3: 1}
for i, joltage in enumerate(input_list):
    joltdiff[joltage - cur_j] = joltdiff[joltage - cur_j] + 1
    cur_j = joltage
answer1 = joltdiff[1] * joltdiff[3]
print("Answer 1:", answer1)

answer2 = 0
diffs = ""
cur_j = 0
for i, joltage in enumerate(input_list):
    diffs += str(joltage - cur_j)
    cur_j = joltage

diffs = "3" + diffs + "3"
diffs = diffs.replace("313", "3")
diffs = diffs.replace("3", "33")
answer2 = int(pow(2, diffs.count("3113"))
              * pow(4, diffs.count("31113"))
              * pow(7, diffs.count("311113")))
print("Answer 2:", answer2)
