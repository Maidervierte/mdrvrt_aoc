""" 2018 aoc07 """

with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = [(x.split(" ")[1], x.split(" ")[7]) for x in f.read().splitlines()]

# input_list = "Step C must be finished before step A can begin.\n" \
#              "Step C must be finished before step F can begin.\n" \
#              "Step A must be finished before step B can begin.\n" \
#              "Step A must be finished before step D can begin.\n" \
#              "Step B must be finished before step E can begin.\n" \
#              "Step D must be finished before step E can begin.\n" \
#              "Step F must be finished before step E can begin.".splitlines()
# input_list = [(x.split(" ")[1], x.split(" ")[7]) for x in input_list]

reqs = {}
steps = set()
for req, step in input_list:
    steps.add(req)
    steps.add(step)
    if step in reqs:
        reqs[step].append(req)
    else:
        reqs[step] = [req]

order = ""

while len(order) != len(steps):
    pos = []
    # print(order)
    for step in [x for x in steps if x not in order]:
        if step not in reqs:
            pos.append(step)
            # print("  ", step)
            continue
        req_found = True
        for req in reqs[step]:
            if req not in order:
                req_found = False
                break
        if req_found:
            pos.append(step)
    #         print("  ", step, reqs[step])
    # print(sorted(pos)[0],pos)
    order += sorted(pos)[0]

print("Answer 1:", order)

order = ""
time = []
timed = []
answer2 = -1
while len(order) != len(steps):
    answer2 += 1
    pos = []
    for i in range(len(time)):
        if time[i] != 0:
            time[i] -= 1
    available = 5 - len(time) + time.count(0)
    for i in range(len(timed)):
        if timed[i] not in order and time[i] == 0:
            order += timed[i]
    if available == 0:
        continue
    for step in [x for x in steps if x not in timed]:
        if step not in reqs:
            pos.append(step)
            continue
        req_found = True
        for req in reqs[step]:
            if req not in order:
                req_found = False
        if req_found:
            pos.append(step)
    for char in sorted(pos)[:available]:
        timed.append(char)
        time.append(ord(char) - 64 + 60)

print("Answer 2:", answer2)
