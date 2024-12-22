""" 2024 aoc22"""

with open("input22.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().splitlines()]

answer1 = 0
answer2 = 0
changes = {}
bananas = {}
for i, line in enumerate(input_list):
    change = []
    banana = []
    secret_number = line
    prev = secret_number
    for _ in range(2000):
        res1 = secret_number << 6
        secret_number ^= res1
        secret_number %= 2 ** 24

        res2 = secret_number >> 5
        secret_number ^= res2
        secret_number %= 2 ** 24

        res3 = secret_number << 11
        secret_number ^= res3
        secret_number %= 2 ** 24

        change.append(int(str(secret_number)[-1]) - int(str(prev)[-1]))
        banana.append(int(str(secret_number)[-1]))
        prev = secret_number
    changes[i] = change
    bananas[i] = banana
    answer1 += secret_number

sequences = {}
for k, v in changes.items():
    temp_sequences = {}
    for i in range(3, len(v)):
        sequence = (v[i - 3], v[i - 2], v[i - 1], v[i])
        if sequence not in temp_sequences:
            temp_sequences[sequence] = [bananas[k][i]]
    for temp_sequence, v in temp_sequences.items():
        if temp_sequence in sequences:
            sequences[temp_sequence] = sequences[temp_sequence] + v
        else:
            sequences[temp_sequence] = v

for k, v in sequences.items():
    answer2 = max(sum(v), answer2)
print("Answer 1:", answer1)
print("Answer 2:", answer2)
