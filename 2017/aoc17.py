""" 2017 aoc17 """

with open("input17.txt", "r", encoding="utf-8") as f:
    input_number = int(f.read())

spinlock = []
index = 0
for x in range(2018):
    spinlock.insert(index + 1, x)
    index += input_number + 1
    index %= len(spinlock)

print("Answer 1:", spinlock[spinlock.index(2017) + 1])

index = 0
answer2 = 0
for x in range(50000000):
    if index == 0:
        answer2 = x
    index += input_number + 1
    index %= (x + 1)

print("Answer 2:", answer2)
