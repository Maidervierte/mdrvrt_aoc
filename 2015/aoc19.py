""" 2015 aoc19 """
import random  # for part 2

with open("input19.txt", "r", encoding="utf-8") as f:
    input_lines = f.read().splitlines()

molecule = input_lines[-1]
repl_dict = {}

for line in input_lines:
    if line == "":
        break
    element, result = line.split(" => ")
    if element in repl_dict:
        temp_set = repl_dict[element]
        temp_set.add(result)
        repl_dict[element] = temp_set
    else:
        temp_set = set()
        temp_set.add(result)
        repl_dict[element] = temp_set


def get_mols(mol, replacements, l_max_len):
    """ get all possible replacement molecules"""
    mols = set()
    i = 0
    while i < (len(mol)):
        cur_elem = ""
        j = 0
        while j < l_max_len:
            if i + j >= len(mol):
                break
            cur_elem += mol[i + j]
            if cur_elem in replacements.keys():
                for replacement in replacements[cur_elem]:
                    new_mol = mol[:i] + replacement + mol[i + len(cur_elem):]
                    mols.add(new_mol)
            j += 1
        i += 1
    return mols


max_len = 0
for key in repl_dict.keys():
    if len(key) > max_len:
        max_len = len(key)

print("Answer 1:", len(get_mols(molecule, repl_dict, max_len)))

rev_repl = {}
for key, values in repl_dict.items():
    for result in values:
        rev_repl[result] = key

max_len = 0
for key in rev_repl.keys():
    if len(key) > max_len:
        max_len = len(key)

attempts = 1000
attempt = 0
min_steps = len(molecule)
while attempt < attempts:
    steps = 0
    temp_mol = molecule
    stop = False
    while not stop:
        random_repl = random.choice(list(rev_repl.keys()))
        if random_repl in temp_mol:
            len_prev = len(temp_mol)
            steps += temp_mol.count(random_repl)
            temp_mol = temp_mol.replace(random_repl, rev_repl[random_repl])
        stop = True
        for key in rev_repl.keys():
            if key in temp_mol:
                stop = False
                break
    if steps < min_steps and temp_mol == "e":
        min_steps = steps
    attempt += 1

print("Answer 2:", min_steps)
