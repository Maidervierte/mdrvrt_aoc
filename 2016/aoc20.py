""" 2016 aoc20 """
with open("input20.txt", "r", encoding="utf-8") as f:
    input_blacklist = f.read().splitlines()

input_blacklist = [x.split("-") for x in input_blacklist]
_blacklist = []
for ip_range in input_blacklist:
    _blacklist.append((int(ip_range[0]), int(ip_range[1])))

_blacklist.sort()
cur_x, cur_y = _blacklist[0]
blacklist = []
for index in range(1, len(_blacklist)):
    if _blacklist[index][0] <= cur_y + 1:
        cur_y = max(cur_y, _blacklist[index][1])
    else:
        blacklist.append((cur_x, cur_y))
        cur_x, cur_y = _blacklist[index]
blacklist.append((cur_x, cur_y))

ip = 0
answer1 = False
allowed = []
while ip <= 4294967295:
    for x, y in blacklist:
        if y >= ip >= x:
            ip = y + 1
        if ip < x:
            break
    if not answer1:
        print("Answer 1:", ip)
        answer1 = True
    allowed.append(ip)
    ip += 1
print("Answer 2:", len(allowed) - 1)
