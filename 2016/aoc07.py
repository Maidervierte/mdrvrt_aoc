""" 2016 aoc07 """
with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


def check_tsl(_ip):
    """checks string for transport-layer snooping"""
    abba = []
    for i in range(len(_ip) - 3):
        if _ip[i] == _ip[i + 3] and _ip[i + 1] == _ip[i + 2] and _ip[i] != _ip[i + 1]:
            abba.append(i)
    if len(abba) == 0:
        return False
    for index in abba:
        for i in range(index, -1, -1):
            if _ip[i] == "]":
                break
            if _ip[i] == "[":
                for j in range(index, len(_ip)):
                    if _ip[j] == "[":
                        break
                    if _ip[j] == "]":
                        return False
                break
    return True


def check_ssl(_ip):
    """checks string for super-secret listening"""
    aba = []
    for i in range(len(_ip) - 2):
        if _ip[i] == _ip[i + 2] and _ip[i] != _ip[i + 1]:
            aba.append(i)
    if len(aba) < 2:
        return False
    inside = []
    outside = []
    for index in aba:
        _outside = True
        for i in range(index, -1, -1):
            if _ip[i] == "]":
                break
            if _ip[i] == "[":
                for j in range(index, len(_ip)):
                    if _ip[j] == "[":
                        break
                    if _ip[j] == "]":
                        inside.append(_ip[index:index + 3])
                        _outside = False
                        break
                break
        if _outside:
            outside.append(_ip[index:index + 3])
    for xyx in inside:
        for yxy in outside:
            if xyx[0] == yxy[1] and yxy[2] == xyx[1]:
                return True
    return False


answer1 = 0
answer2 = 0
for ip in input_list:
    if check_tsl(ip):
        answer1 += 1
    if check_ssl(ip):
        answer2 += 1

print("Answer 1:", answer1)
print("Answer 2:", answer2)
