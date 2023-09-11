""" 2017 aoc24 """
with open("input24.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

pairs = set()
for line in input_list:
    pairs.add(tuple(int(x) for x in line.split("/")))

bridges = set()
for (x, y) in pairs:
    if x == 0:
        bridges.add(((x, y),))

new_bridges = set()
all_bridges = set()
check = 0
for _ in range(len(input_list)):
    new_bridges = set()
    for bridge in bridges:
        temp = pairs.copy()
        chain = [bridge[0][1]]
        for pair in bridge:
            if 0 not in pair:
                if pair[0] == pair[1]:
                    chain.append(pair[0])
                else:
                    if pair[0] == chain[-1]:
                        chain.append(pair[1])
                    else:
                        chain.append(pair[0])
            else:
                chain.append(pair[1])
            temp.remove(pair)
        for pair in [(x, y) for (x, y) in temp if x == chain[-1] or y == chain[-1]]:
            new_bridges.add((*bridge, pair))
            all_bridges.add((*bridge, pair))
    bridges = new_bridges.copy()

longest = 0
for bridge in all_bridges:
    longest = max(longest, len(bridge))
max_sum = 0
max_sum_longest = 0
for bridge in all_bridges:
    cur_sum = 0
    cur_sum_longest = 0
    for pair in bridge:
        cur_sum += pair[0] + pair[1]
        if len(bridge) == longest:
            cur_sum_longest += pair[0] + pair[1]
    max_sum = max(cur_sum, max_sum)
    max_sum_longest = max(cur_sum_longest, max_sum_longest)
print("Answer 1:", max_sum)
print("Answer 2:", max_sum_longest)
