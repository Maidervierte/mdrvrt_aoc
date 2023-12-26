""" 2023 aoc21 """

with open("input21.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

garden = {}
start = (0, 0)
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        garden[i, j] = char
        if char == "S":
            start = (i, j)

visited = set()
visited.add(start)

for _ in range(64):
    temp = set()
    for i, j in visited:
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (x, y) in garden and garden[x, y] != "#":
                temp.add((x, y))
    visited = temp
print("Answer 1:", len(visited))

max_i = len(input_list) - 1
max_j = len(input_list[0]) - 1

visited = set()
current = set()
visited.add((*start, 0, 0))
current.add((*start, 0, 0))
odds = 0
evens = 1
answer2 = []
steps = 0
loop_length = 11
counter = 6
while steps < 1000:
    temp = set()
    for (i, j, m, n) in current:
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            _m = m
            _n = n
            if x < 0:
                x = max_i
                _m = m - 1
            if x > max_i:
                x = 0
                _m = m + 1
            if y < 0:
                y = max_j
                _n = n - 1
            if y > max_j:
                y = 0
                _n = n + 1
            if garden[x, y] != "#" and (x, y, _m, _n) not in visited:
                temp.add((x, y, _m, _n))
                visited.add((x, y, _m, _n))
    current = temp
    answer2.append(len(temp))
    steps += 1

loop = False
for loop_length in range(5, len(answer2) // 3):
    for loop_start in range(len(answer2)):
        if loop_start + (3 * loop_length) >= len(answer2):
            break
        loop = True
        key = []
        for j in range(loop_length):
            key.append(answer2[loop_start + j + loop_length] - answer2[loop_start + j])
            if answer2[loop_start + j + loop_length] - answer2[loop_start + j] != answer2[
                loop_start + j + 2 * loop_length] - answer2[loop_start + j + loop_length]:
                loop = False
                break
        if loop:
            break
    if loop:
        break

visited = set()
current = set()
visited.add((*start, 0, 0))
current.add((*start, 0, 0))
odds = 0
evens = 1
counter = (loop_start % loop_length)
answer2 = [0] * loop_length
steps = 0
while steps < 26501365:
    if steps <= loop_start + loop_length:
        temp = set()
        for (i, j, m, n) in current:
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                _m = m
                _n = n
                if x < 0:
                    x = max_i
                    _m = m - 1
                if x > max_i:
                    x = 0
                    _m = m + 1
                if y < 0:
                    y = max_j
                    _n = n - 1
                if y > max_j:
                    y = 0
                    _n = n + 1
                if garden[x, y] != "#" and (x, y, _m, _n) not in visited:
                    temp.add((x, y, _m, _n))
                    visited.add((x, y, _m, _n))
        current = temp
        answer2[counter] = len(temp)
    else:
        answer2[counter] += key[counter]
    if steps % 2 == 0:
        odds += answer2[counter]
    else:
        evens += answer2[counter]
    counter += 1
    if counter == loop_length:
        counter = 0
    steps += 1

if steps % 2 != 0:
    print("Answer 2:", odds)
else:
    print("Answer 2:", evens)
