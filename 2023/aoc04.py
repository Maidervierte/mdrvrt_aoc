""" 2023 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

matches = {}
answer1 = 0
won_cards = []
for i, line in enumerate(input_list):
    won_cards.append(i + 1)
    intersection = set(int(x) for x in line.split(" | ")[0].split(": ")[1].split(" ") if x != "") \
        .intersection(int(x) for x in line.split(" | ")[1].split(" ") if x != "")
    matches[i + 1] = len(intersection)
    if len(intersection)>0:
        points = 2 ** (len(intersection) - 1)
        answer1 += points

print("Answer 1:", answer1)

i = 0
while i < len(won_cards):
    cur_card = won_cards[i]
    intersection = matches[cur_card]
    for x in range(intersection):
        won_cards.append(cur_card + x + 1)
    i += 1

print("Answer 2:", len(won_cards))
