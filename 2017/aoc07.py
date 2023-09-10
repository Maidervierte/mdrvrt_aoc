""" 2017 aoc07 """

with open("input07.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

# input_lines = "pbga (66)\n" \
#               "xhth (57)\n" \
#               "ebii (61)\n" \
#               "havc (66)\n" \
#               "ktlj (57)\n" \
#               "fwft (72) -> ktlj, cntj, xhth\n" \
#               "qoyq (66)\n" \
#               "padx (45) -> pbga, havc, qoyq\n" \
#               "tknk (41) -> ugml, padx, fwft\n" \
#               "jptl (61)\n" \
#               "ugml (68) -> gyxo, ebii, jptl\n" \
#               "gyxo (61)\n" \
#               "cntj (57)".splitlines()
left = set()
right = set()
programs = {}
for line in input_lines:
    left.add(line.split(" (")[0])
    if len(line.split(" -> ")) == 2:
        programs[line.split(" (")[0]] = [int(line.split(" (")[1].split(")")[0])]
        for program in line.split(" -> ")[1].split(","):
            right.add(program.strip())
            programs[line.split(" (")[0]].append(program.strip())
    else:
        programs[line.split(" (")[0]] = [int(line.split(" (")[1][:-1])]

root = str(left.difference(right))[2:-2]
print("Answer 1:", root)

left.difference(right)


def get_weight(key):
    weight = programs[key][0]
    if len(programs[key]) > 1:
        for _program in programs[key][1:]:
            weight += get_weight(_program)
    return weight


cur_prog = root
prev = root
while True:
    cur_progs = []
    for program in programs[cur_prog][1:]:
        cur_progs.append(get_weight(program))
    odd_one = min(cur_progs, key=cur_progs.count)
    if odd_one != max(cur_progs, key=cur_progs.count):
        cur_prog = programs[cur_prog][1:][cur_progs.index(odd_one)]
    else:
        print("Answer 2:", prev[0][0] - (min(prev[1], key=prev[1].count) - max(prev[1], key=prev[1].count)))
        break
    prev = (programs[cur_prog], cur_progs)
