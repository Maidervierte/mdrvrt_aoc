""" 2023 aoc25 """
import copy
import sys
from itertools import combinations
from multiprocessing import Pool
from collections import Counter
import random

sys.setrecursionlimit(2000)


def count_connections(start_wire):
    """counts connections on path between wires"""
    _wires = start_wire[2]
    goal_wire = start_wire[1]
    queue = [(start_wire[0],)]
    _c = Counter()
    while queue:
        temp = []
        for cur_path in queue:
            cur_wire = cur_path[-1]
            for next_wire in _wires[cur_wire]:
                if next_wire == goal_wire:
                    cur_path += (next_wire,)
                    break
                if next_wire not in cur_path:
                    temp.append(cur_path + (next_wire,))
            if next_wire == goal_wire:
                break
        if goal_wire in cur_path:
            break
        queue = temp
    to_add = []
    for _i, link in enumerate(cur_path[:-1]):
        to_add.append((min(cur_path[_i + 1], link), max(cur_path[_i + 1], link)))
    _c.update(to_add)
    return _c


def get_connected(check_wire, _wires, connected_wires):
    """checks connected wires"""
    connected_wires.add(check_wire)
    for new_wire in _wires[check_wire]:
        if new_wire not in connected_wires:
            connected_wires = connected_wires.union(get_connected(new_wire, _wires, connected_wires))
    return connected_wires


def check_combs(combs):
    ((w1, w4), (w2, w5), (w3, w6)) = combs[0]
    temp = copy.deepcopy(combs[1])
    temp[w1].remove(w4)
    temp[w4].remove(w1)
    temp[w2].remove(w5)
    temp[w5].remove(w2)
    temp[w3].remove(w6)
    temp[w6].remove(w3)
    w1set = get_connected(w1, temp, set())
    if w4 in w1set:
        return
    w2set = get_connected(w4, temp, set())
    answer = len(w1set) * len(w2set)
    print("Answer:", answer)


if __name__ == '__main__':
    with open("input25.txt", "r", encoding="utf-8") as f:
        input_list = f.read().splitlines()

    wires = {}

    for line in input_list:
        line = line.split(": ")
        w1 = line[0]
        if w1 in wires:
            for wire in line[1].split(" "):
                wires[w1].add(wire)
        else:
            wires[w1] = set()
            for wire in line[1].split(" "):
                wires[w1].add(wire)
        for wire in line[1].split(" "):
            if wire in wires:
                wires[wire].add(w1)
            else:
                wires[wire] = set()
                wires[wire].add(w1)

    c = Counter()
    wire_pairs = []
    for _ in range(50):
        sw = random.choice(list(wires.keys()))
        gw = random.choice(list(wires.keys()))
        if sw != gw:
            wire_pairs.append((sw, gw))
    with Pool(8) as p:
        for c_add in p.map(count_connections, [[x, y, wires] for x, y in wire_pairs]):
            c += c_add
    wire_combs = []
    for pair in list(c.most_common()[:10]):
        wire_combs.append(pair[0])
    counter = 0
    sys.setrecursionlimit(2000)
    with Pool(8) as p:
        p.map(check_combs, [[x, wires] for x in combinations(wire_combs, 3)])
