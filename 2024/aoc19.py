""" 2024 aoc19"""

with open("input19.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
patterns = sorted(input_list[0].split(", "), key=len)
designs = input_list[2:]


def iterate(d):
    """iterates"""
    if d == "":
        return ""
    if d in visited:
        return d
    c = [x for x in patterns if len(x) <= len(d) and d[:len(x)] == x]
    for p in c:
        _d = d.replace(p, "", 1)
        if _d == "":
            return ""
        if iterate(_d) == "":
            return ""
        visited.add(_d)
    return d


design_counter = {}
for i, design in enumerate(designs):
    visited = set()
    ways = [0]
    if iterate(design) == "":
        answer1 += 1
        cur_designs = {design: 1}
        all_designs = {design: 1}
        for _ in range(len(patterns)):
            temp = {}
            for cur_design, counter in cur_designs.items():
                cur_patterns = [x for x in patterns if
                                len(x) <= len(cur_design) and
                                cur_design[:len(x)] == x]
                for cur_pattern in cur_patterns:
                    rest = cur_design.replace(cur_pattern, "", 1)
                    if temp.get(rest, 0) == 0:
                        temp[rest] = counter
                    else:
                        temp[rest] += counter
                    if all_designs.get(rest, 0) == 0:
                        all_designs[rest] = counter
                    else:
                        all_designs[rest] += counter
            if not temp:
                break
            cur_designs = dict(temp)
        answer2 += all_designs[""]
print("Answer 1:", answer1)
print("Answer 2:", answer2)
