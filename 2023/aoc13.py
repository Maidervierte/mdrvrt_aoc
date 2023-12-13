""" 2023 aoc13 """

with open("input13.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

mirrors = []
mirror = []
for i, line in enumerate(input_list):
    if line == "":
        mirrors.append(mirror)
        mirror = []
    else:
        mirror.append(line)
mirrors.append(mirror)


def not_similar_enough(m1, m2):
    """checks if line arent too enough"""
    diff_count = 0
    for _i, char in enumerate(m1):
        if char != m2[_i]:
            diff_count += 1
    if diff_count > 1:
        return True
    return False


def check_symmetry(_mirror, _i, p2):
    """checks if symmetry holds"""
    if p2:
        j = i + 2
        _i -= 1
        while _i >= 0 and j < len(_mirror):
            if not_similar_enough(mirror[_i], mirror[j]):
                return False
            _i -= 1
            j += 1
        return True
    j = i + 2
    _i -= 1
    while _i >= 0 and j < len(_mirror):
        if _mirror[_i] != _mirror[j]:
            return False
        _i -= 1
        j += 1
    return True


sym_lines = []
rows = []
lines = []
for m, mirror in enumerate(mirrors):
    mirror_found = False
    for i, line in enumerate(mirror[:-1]):
        if line == mirror[i + 1]:
            if check_symmetry(mirror, i, False):
                mirror_found = True
                rows.append(i + 1)
                sym_lines.append(("r", i + 1))
                break
    if mirror_found:
        continue
    mirror = list(map(list, zip(*mirror)))
    for i, line in enumerate(mirror[:-1]):
        if line == mirror[i + 1]:
            if check_symmetry(mirror, i, False):
                lines.append(i + 1)
                sym_lines.append(("l", i + 1))
                break

print("Answer 1:", sum(lines) + 100 * sum(rows))

rows = []
lines = []
for m, mirror in enumerate(mirrors):
    mirror_found = False
    for i, line in enumerate(mirror[:-1]):
        if line == mirror[i + 1] and (sym_lines[m][0] != "r" or sym_lines[m][1] != i + 1):
            if check_symmetry(mirror, i, True):
                mirror_found = True
                rows.append(i + 1)
                break
    if mirror_found:
        continue
    mirror = list(map(list, zip(*mirror)))
    for i, line in enumerate(mirror[:-1]):
        if line == mirror[i + 1] and (sym_lines[m][0] != "l" or sym_lines[m][1] != i + 1):
            if check_symmetry(mirror, i, True):
                lines.append(i + 1)
                break
    if mirror_found:
        continue
    mirror = list(map(list, zip(*mirror)))
    for i, line in enumerate(mirror[:-1]):
        if not not_similar_enough(line, mirror[i + 1]) and (
                sym_lines[m][0] != "r" or sym_lines[m][1] != i + 1):
            if check_symmetry(mirror, i, False):
                rows.append(i + 1)
                break
    if mirror_found:
        continue
    mirror = list(map(list, zip(*mirror)))
    for i, line in enumerate(mirror[:-1]):
        if not not_similar_enough(line, mirror[i + 1]) and (
                sym_lines[m][0] != "l" or sym_lines[m][1] != i + 1):
            if check_symmetry(mirror, i, False):
                lines.append(i + 1)
                break

print("Answer 2:", sum(lines) + 100 * sum(rows))
