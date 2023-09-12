""" 2018 aoc09 """
with open("input09.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split(" ")

players, last_marble = int(input_list[0]), int(input_list[6])

cur_player = 0
cur_marble = 0
marbles = []
scores = [0 for x in range(players)]
marble = 0
last_added = marble
while marble in range(last_marble + 1):
    if marble != 0 and marble % 23 == 0:
        scores[cur_player - 1] += marble
        cur_marble -= 8
        if cur_marble < 0:
            cur_marble = len(marbles) + cur_marble
        scores[cur_player - 1] += marbles.pop(cur_marble)
        cur_marble += 1
        if cur_marble >= len(marbles):
            cur_marble %= len(marbles)
        marble = last_added + 1
        last_added = marble
    else:
        marbles.insert(cur_marble + 1, marble)
        cur_marble += 2
        if cur_marble >= len(marbles):
            cur_marble %= len(marbles)
        marble = last_added + 1
        last_added = marble
    cur_player += 1
    if cur_player > players:
        cur_player = 1
print("Answer 1:", max(scores))

cur_player = 0
cur_marble = 0
marbles = []
scores = [0 for x in range(players)]
marble = 0
last_added = marble
last_marble *= 100
# double linked list would be smarter, but I'd need to implement that
# and computer time is worth less than mine and this is fast enough
while marble in range(last_marble + 1):
    len_marbles = len(marbles)
    if marble != 0 and marble % 23 == 0:
        scores[cur_player - 1] += marble
        cur_marble -= 8
        if cur_marble < 0:
            cur_marble = len_marbles + cur_marble
        scores[cur_player - 1] += marbles.pop(cur_marble)
        cur_marble += 1
        if cur_marble >= len_marbles - 1:
            cur_marble %= (len_marbles - 1)
        marble = last_added + 1
        last_added = marble
    else:
        marbles.insert(cur_marble + 1, marble)
        cur_marble += 2
        if cur_marble >= len_marbles + 1:
            cur_marble %= (len_marbles + 1)
        marble = last_added + 1
        last_added = marble
    cur_player += 1
    if cur_player > players:
        cur_player = 1
print("Answer 2:", max(scores))
