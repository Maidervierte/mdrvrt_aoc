""" 2023 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

matches = {}
answer1 = 0
won_cards = []
for i, line in enumerate(input_list):
    won_cards.append(1)
    intersection = set(int(x) for x in line.split(" | ")[0].split(": ")[1].split()) \
        .intersection(int(x) for x in line.split(" | ")[1].split())
    matches[i + 1] = len(intersection)
    if len(intersection) > 0:
        points = 2 ** (len(intersection) - 1)
        answer1 += points

print("Answer 1:", answer1)

for i in range(len(won_cards)):
    for x in range(matches[i + 1]):
        won_cards[i + x + 1] += won_cards[i]

print("Answer 2:", sum(won_cards))
