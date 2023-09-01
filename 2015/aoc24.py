""" 2015 aoc24 """

from itertools import combinations
import math

with open("input24.txt", "r", encoding="utf-8") as f:
    weights = [int(x) for x in f.read().splitlines()]

needed_weight = sum(weights) // 3
lengths = [0] * len(weights)

pos_combs = [[] for x in range(len(weights))]
for x in range(len(weights)):
    for comb in filter(lambda e: sum(e) == needed_weight, combinations(weights, x)):
        pos_combs[len(list(comb))].append(set(comb))
        lengths[len(list(comb))] += 1

pos_lengths = []
for i, length in enumerate(lengths):
    if length != 0:
        pos_lengths.append(i)

found = False
for i in range(len(weights)):
    pos_group1s = sorted(pos_combs[i], key=lambda x: math.prod(x))
    leng_combs = list(filter(lambda e: sum(e) + i == len(weights),
                             combinations(pos_lengths, 2)))
    for group1 in pos_group1s:
        if found:
            break
        for leng_comb in leng_combs:
            if found:
                break
            for group2 in pos_combs[leng_comb[0]]:
                if found:
                    break
                if group2.isdisjoint(group1):
                    for group3 in pos_combs[leng_comb[1]]:
                        if found:
                            break
                        if group3.isdisjoint(group1) and group3.isdisjoint(group2):
                            print("Answer 1:", math.prod(group1))
                            print(group1, group2, group3)
                            found = True
    if found:
        break

needed_weight = sum(weights) // 4
lengths = [0] * len(weights)

pos_combs = [[] for x in range(len(weights))]
for x in range(len(weights)):
    for comb in filter(lambda e: sum(e) == needed_weight, combinations(weights, x)):
        pos_combs[len(list(comb))].append(set(comb))
        lengths[len(list(comb))] += 1

pos_lengths = []
for i, length in enumerate(lengths):
    if length != 0:
        pos_lengths.append(i)

found = False
for i in range(len(weights)):
    pos_group1s = sorted(pos_combs[i], key=lambda x: math.prod(x))
    leng_combs = list(filter(lambda e: sum(e) + i == len(weights),
                             combinations(pos_lengths, 3)))
    if len(leng_combs) == 0:
        continue
    for group1 in pos_group1s:
        if found:
            break
        for leng_comb in leng_combs:
            if found:
                break
            for group2 in pos_combs[leng_comb[0]]:
                if found:
                    break
                if group2.isdisjoint(group1):
                    for group3 in pos_combs[leng_comb[1]]:
                        if found:
                            break
                        if group3.isdisjoint(group1) and group3.isdisjoint(group2):
                            for group4 in pos_combs[leng_comb[2]]:
                                if found:
                                    break
                                if group4.isdisjoint(group1) and \
                                        group4.isdisjoint(group2) and \
                                        group4.isdisjoint(group3):
                                    print("Answer 2:", math.prod(group1))
                                    found = True
    if found:
        break
