""" 2015 aoc13 """
from itertools import permutations

with open("input13.txt", "r", encoding="utf-8") as f:
    happiness = f.read().splitlines()

hap_dict = {}
name_set = set()
for line in happiness:
    name1, _, op, amount, _, _, _, _, _, _, name2 = line.split(" ")
    name_set.add(name1)
    if name1 not in hap_dict:
        hap_dict[name1] = {}
    if op == "lose":
        hap_dict[name1][name2[:-1]] = -int(amount)
    else:
        hap_dict[name1][name2[:-1]] = int(amount)

perms = list(permutations(name_set))
max_hap = 0
for perm in perms:
    hap_sum = 0
    for i in range(len(perm) - 1):
        hap_sum += hap_dict[perm[i]][perm[i + 1]]
        hap_sum += hap_dict[perm[i + 1]][perm[i]]
    hap_sum += hap_dict[perm[0]][perm[-1]]
    hap_sum += hap_dict[perm[-1]][perm[0]]
    if hap_sum > max_hap:
        max_hap = hap_sum

print("Answer 1:", max_hap)

hap_dict["Me"]={}
for name in name_set:
    hap_dict[name]["Me"] = 0
    hap_dict["Me"][name] = 0
name_set.add("Me")

perms = list(permutations(name_set))
max_hap = 0
for perm in perms:
    hap_sum = 0
    for i in range(len(perm) - 1):
        hap_sum += hap_dict[perm[i]][perm[i + 1]]
        hap_sum += hap_dict[perm[i + 1]][perm[i]]
    hap_sum += hap_dict[perm[0]][perm[-1]]
    hap_sum += hap_dict[perm[-1]][perm[0]]
    if hap_sum > max_hap:
        max_hap = hap_sum

print("Answer 2:", max_hap)
