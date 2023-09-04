""" 2016 aoc16 """

with open("input16.txt", "r", encoding="utf-8") as f:
    initial_state = f.read()

max_len = 272
cur_state = initial_state
translation = {48: 49, 49: 48}
while len(cur_state) < max_len:
    a = cur_state
    b = a[::-1].translate(translation)
    cur_state = a + "0" + b

cur_state = cur_state[:max_len]
check_sum = cur_state
while len(check_sum) % 2 == 0:
    _check_sum = []
    check_sum = list(check_sum)
    while len(check_sum) != 0:
        if check_sum.pop() == check_sum.pop():
            _check_sum.append("1")
        else:
            _check_sum.append("0")
    check_sum = "".join(_check_sum)[::-1]

print("Answer 1:", check_sum)

max_len = 35651584
cur_state = initial_state
translation = {48: 49, 49: 48}
while len(cur_state) < max_len:
    b = cur_state[::-1].translate(translation)
    cur_state = cur_state + "0" + b

cur_state = cur_state[:max_len]
check_sum = cur_state
while len(check_sum) % 2 == 0:
    _check_sum = []
    check_sum = list(check_sum)
    while len(check_sum) != 0:
        if check_sum.pop() == check_sum.pop():
            _check_sum.append("1")
        else:
            _check_sum.append("0")
    check_sum = "".join(_check_sum)[::-1]

print("Answer 1:", check_sum)
