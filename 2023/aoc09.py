""" 2023 aoc09 """

with open("input09.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

histories = []

for line in input_list:
    histories.append([int(x) for x in line.split()])

answer1 = 0
for history in histories:
    cur_history = history
    last_values = [cur_history[-1]]
    while len(set(cur_history)) != 1:
        temp_history = []
        cur_value = cur_history[0]
        for x in cur_history[1:]:
            temp_history.append(x - cur_value)
            cur_value = x
        cur_history = temp_history
        last_values.append(cur_history[-1])
    last_value = 0
    for x in reversed(last_values):
        last_value += x
    answer1 += last_value
print("Answer 1:", answer1)

answer2 = 0
for history in histories:
    cur_history = history
    first_values = [cur_history[0]]
    while len(set(cur_history)) != 1:
        temp_history = []
        cur_value = cur_history[0]
        for x in cur_history[1:]:
            temp_history.append(x - cur_value)
            cur_value = x
        cur_history = temp_history
        first_values.append(cur_history[0])
    first_value = first_values[-1]
    for x in reversed(first_values[:-1]):
        first_value = x - first_value
    answer2 += first_value
print("Answer 2:", answer2)
