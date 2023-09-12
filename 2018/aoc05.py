""" 2018 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_polymers = f.read()

old_polymer = input_polymers
index = 0
for x in range(len(old_polymer)):
    i = max(index - 2, 0)
    new_polymer = old_polymer[:i]
    index = 0
    old_len = len(old_polymer)
    while i in range(old_len - 1):
        if old_polymer[i].isupper():
            if not old_polymer[i + 1].isupper() and old_polymer[i] == old_polymer[i + 1].upper():
                new_polymer += old_polymer[i + 2:]
                index = i
                break
            new_polymer += old_polymer[i]
            if i == old_len - 2:
                new_polymer += old_polymer[-1]
            i += 1
        elif old_polymer[i + 1].isupper() and old_polymer[i].upper() == old_polymer[i + 1]:
            new_polymer += old_polymer[i + 2:]
            index = i
            break
        else:
            new_polymer += old_polymer[i]
            if i == old_len - 2:
                new_polymer += old_polymer[-1]
            i += 1
    if old_polymer == new_polymer:
        break
    old_polymer = new_polymer

print("Answer 1:", len(old_polymer))

letters = []
for x in range(65, 91):
    letters.append((chr(x), chr(x + 32)))

min_len = len(old_polymer)

for pair in letters:
    old_polymer = input_polymers
    for letter in pair:
        old_polymer = old_polymer.replace(letter, "")
    index = 0
    for x in range(len(old_polymer)):
        i = max(index - 2, 0)
        new_polymer = old_polymer[:i]
        if x > 19550:
            pass
        index = 0
        old_len = len(old_polymer)
        while i in range(old_len - 1):
            if old_polymer[i].isupper():
                if not old_polymer[i + 1].isupper() and old_polymer[i] == old_polymer[i + 1].upper():
                    new_polymer += old_polymer[i + 2:]
                    index = i
                    break
                new_polymer += old_polymer[i]
                if i == old_len - 2:
                    new_polymer += old_polymer[-1]
                i += 1
            elif old_polymer[i + 1].isupper() and old_polymer[i].upper() == old_polymer[i + 1]:
                new_polymer += old_polymer[i + 2:]
                index = i
                break
            else:
                new_polymer += old_polymer[i]
                if i == old_len - 2:
                    new_polymer += old_polymer[-1]
                i += 1
        if old_polymer == new_polymer:
            break
        old_polymer = new_polymer
    min_len = min(min_len, len(old_polymer))

print("Answer 2:", min_len)
