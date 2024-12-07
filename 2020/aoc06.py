""" 2020 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = [x.split("\n") for x in f.read().split("\n\n")]

answer1 = 0
answer2 = 0
for group in input_list:
    yes = set()
    yes_all = set(group[0])
    for person in group:
        yes = yes.union(set(person))
        yes_all = yes_all.intersection(set(person))
    answer1 += len(yes)
    answer2 += len(yes_all)
print("Answer 1:", answer1)
print("Answer 2:", answer2)
