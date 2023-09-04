""" 2016 aoc11 """
from itertools import combinations

with open("input11.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

building = [set() for x in range(len(input_lines))]

things = ["", ""]
for line in input_lines:
    line_split = line.split(" ")
    line_split = line_split[4:]
    if "and" in line_split:
        line_split.remove("and")
    if len(line_split) == 2:
        continue
    for i in range(0, len(line_split), 3):
        things.append(line_split[i] + " " + line_split[i + 1] + " " + line_split[i + 2])

for i, line in enumerate(input_lines):
    line_split = line.split(" ")
    line_split = line_split[4:]
    if "and" in line_split:
        line_split.remove("and")
    if len(line_split) == 2:
        continue
    for j in range(0, len(line_split), 3):
        index = things.index(line_split[j] + " " + line_split[j + 1] + " " + line_split[j + 2])
        abbr = things[index].split(" ")[1][:2] + "_" + things[index].split(" ")[2][:1]
        building[i].add(abbr)


def check_rad(__building):
    """checks if any floor is invalid"""
    for _floor in __building:
        for _elem in _floor:
            if _elem[-1] == "m":
                if _elem[:2] + "g" in _floor:
                    continue
                for __elem in _floor:
                    if __elem[-1] == "g":
                        return True
    return False


def normalize(__building):
    """normalizes building because it doesnt matter which pair is which"""
    normalized = set()
    _index = 0
    new_building = [set() for x in range(len(__building[2:]))]
    for _i, _floor in enumerate(__building[2:]):
        for _elem in _floor:
            if _elem.split("_")[0] in normalized:
                continue
            new_building[_i].add(str(_index) + "_" + _elem.split("_")[1])
            for _j, __floor in enumerate(__building[2:]):
                for __elem in __floor:
                    if _elem.split("_")[0] == __elem.split("_")[0] and _elem != __elem:
                        new_building[_j].add(str(_index) + "_" + __elem.split("_")[1])
            normalized.add(_elem.split("_")[0])
            _index += 1
    new_building = [frozenset(x) for x in new_building]
    new_building.insert(0, __building[1])
    new_building.insert(0, __building[0])
    return new_building


building = [frozenset(x) for x in building]
building.insert(0, 1)
building.insert(0, 0)
building = normalize(building)
states = set()
states.add(tuple(building))
all_states = set()
all_states.add(tuple(building[1:]))
solutions = []
found = False
while not found:
    new_states = set()
    for state in states:
        _building = [set(x) for x in state[2:]]
        _building.insert(0, state[1])
        _building.insert(0, state[0])
        if len(_building[2]) + len(_building[3]) + len(_building[4]) == 0:
            solutions.append(state)
            found = True
        moves = []
        combs = list(combinations(_building[_building[1] + 1], 2))
        combs = [list(x) for x in combs]
        for elem in _building[_building[1] + 1]:
            combs.append([elem])
        for comb in combs:
            moves.append([_building[1], comb])
        for move in moves:
            temp_building = [_building[0], _building[1]]
            for x in _building[2:]:
                temp_building.append(set(x))
            start_floor = move[0]
            elems = move[1]
            for i in range(start_floor, 4):
                for elem in elems:
                    temp_building[i + 1].remove(elem)
                    temp_building[i + 1 + 1].add(elem)
                temp_building[0] += 1
                temp_building[1] += 1
                normalized_building = normalize([temp_building[0], temp_building[1], frozenset(temp_building[2]),
                                                 frozenset(temp_building[3]), frozenset(temp_building[4]),
                                                 frozenset(temp_building[5])])
                if tuple(normalized_building[1:]) in all_states:
                    continue
                if check_rad(temp_building[2:]):
                    break
                new_states.add(tuple(normalized_building))
            temp_building = [_building[0], _building[1]]
            for x in _building[2:]:
                temp_building.append(set(x))
            for i in range(start_floor, 1, -1):
                for elem in elems:
                    temp_building[i + 1].remove(elem)
                    temp_building[i + 1 - 1].add(elem)
                temp_building[0] += 1
                temp_building[1] -= 1
                normalized_building = normalize([temp_building[0], temp_building[1], frozenset(temp_building[2]),
                                                 frozenset(temp_building[3]), frozenset(temp_building[4]),
                                                 frozenset(temp_building[5])])
                if tuple(normalized_building[1:]) in all_states:
                    continue
                if check_rad(temp_building[2:]):
                    break
                new_states.add(tuple(normalized_building))
    states = set(new_states)
    for state in states:
        all_states.add(state[1:])

min_steps = 9999
for solution in solutions:
    if solution[0] < min_steps:
        min_steps = solution[0]
print("Answer 1:", min_steps)

new_elems = set(building[2])
new_elems.add("el_g")
new_elems.add("el_m")
new_elems.add("di_g")
new_elems.add("di_m")
building[2] = frozenset(new_elems)
building = normalize(building)
states = set()
states.add(tuple(building))
all_states = set()
all_states.add(tuple(building[1:]))
solutions = []
found = False
while not found:
    new_states = set()
    for state in states:
        _building = [set(x) for x in state[2:]]
        _building.insert(0, state[1])
        _building.insert(0, state[0])
        if len(_building[2]) + len(_building[3]) + len(_building[4]) == 0:
            solutions.append(state)
            found = True
        moves = []
        combs = list(combinations(_building[_building[1] + 1], 2))
        combs = [list(x) for x in combs]
        for elem in _building[_building[1] + 1]:
            combs.append([elem])
        for comb in combs:
            moves.append([_building[1], comb])
        for move in moves:
            temp_building = [_building[0], _building[1]]
            for x in _building[2:]:
                temp_building.append(set(x))
            start_floor = move[0]
            elems = move[1]
            for i in range(start_floor, 4):
                for elem in elems:
                    temp_building[i + 1].remove(elem)
                    temp_building[i + 1 + 1].add(elem)
                temp_building[0] += 1
                temp_building[1] += 1
                normalized_building = normalize([temp_building[0], temp_building[1], frozenset(temp_building[2]),
                                                 frozenset(temp_building[3]), frozenset(temp_building[4]),
                                                 frozenset(temp_building[5])])
                if tuple(normalized_building[1:]) in all_states:
                    continue
                if check_rad(temp_building[2:]):
                    break
                new_states.add(tuple(normalized_building))
            temp_building = [_building[0], _building[1]]
            for x in _building[2:]:
                temp_building.append(set(x))
            for i in range(start_floor, 1, -1):
                for elem in elems:
                    temp_building[i + 1].remove(elem)
                    temp_building[i + 1 - 1].add(elem)
                temp_building[0] += 1
                temp_building[1] -= 1
                normalized_building = normalize([temp_building[0], temp_building[1], frozenset(temp_building[2]),
                                                 frozenset(temp_building[3]), frozenset(temp_building[4]),
                                                 frozenset(temp_building[5])])
                if tuple(normalized_building[1:]) in all_states:
                    continue
                if check_rad(temp_building[2:]):
                    break
                new_states.add(tuple(normalized_building))
    states = set(new_states)
    for state in states:
        all_states.add(state[1:])

min_steps = 9999
for solution in solutions:
    if solution[0] < min_steps:
        min_steps = solution[0]
print("Answer 2:", min_steps)