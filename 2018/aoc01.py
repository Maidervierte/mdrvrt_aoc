""" 2018 aoc01 """
with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

score = 0
score_set = set()
score_set.add(score)
twice = False
while not twice:
    for x in input_list:
        score = eval(str(score) + x)
        if score in score_set:
            twice = True
            duplicate = score
            break
        else:
            score_set.add(score)
score = 0
for x in input_list:
    score = eval(str(score) + x)
print("Answer 1:", score)
print("Answer 2:", duplicate)
