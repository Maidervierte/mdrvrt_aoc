""" 2016 aoc21 """
from itertools import permutations

with open("input21.txt", "r", encoding="utf-8") as f:
    operations = f.read().splitlines()

password = "abcdefgh"


def scramble(_password):
    """scrambles password"""
    for operation in operations:
        op = operation.split(" ")[0]
        match op:
            case "rotate":
                match operation.split(" ")[1]:
                    case "left":
                        steps = int(operation.split(" ")[2])
                        _password = _password[steps:] + _password[:steps]
                    case "right":
                        steps = int(operation.split(" ")[2])
                        _password = _password[-steps:] + _password[:-steps]
                    case "based":
                        temp = list(_password)
                        index = temp.index(operation.split(" ")[-1])
                        _password = _password[-1:] + _password[:-1]
                        _password = _password[-index:] + _password[:-index]
                        if index >= 4:
                            _password = _password[-1:] + _password[:-1]
            case "swap":
                if operation.split(" ")[1] == "position":
                    i1 = int(operation.split(" ")[2])
                    i2 = int(operation.split(" ")[5])
                    temp = list(_password)
                    temp_char = temp[i1]
                    temp[i1] = temp[i2]
                    temp[i2] = temp_char
                    _password = "".join(temp)
                else:
                    if operation.split(" ")[1] == "letter":
                        i1 = operation.split(" ")[2]
                        i2 = operation.split(" ")[5]
                        temp = _password.replace(i1, "1").replace(i2, i1)
                        _password = temp.replace("1", i2)
            case "reverse":
                i1 = int(operation.split(" ")[2])
                i2 = int(operation.split(" ")[4])
                reverse = _password[i1:i2 + 1]
                _password = _password[:i1] + reverse[::-1] + _password[i2 + 1:]
            case "move":
                i1 = int(operation.split(" ")[2])
                i2 = int(operation.split(" ")[5])
                temp = list(_password)
                temp.insert(i2, temp.pop(i1))
                _password = "".join(temp)
    return _password


print("Answer 1:", scramble(password))

scrambled = "fbgdceah"

for perm in permutations(list(scrambled)):
    perm = "".join(perm)
    if scramble(perm) == scrambled:
        print("Answer 2:", perm)
        break
