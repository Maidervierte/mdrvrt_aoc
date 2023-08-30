""" 2015 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    string_list = f.read().splitlines()


def vowels(string):
    """ counts vowels """
    number = string.count("a") + string.count("e") + string.count("i") + \
             string.count("o") + string.count("u")
    return number > 2


def doubles(string):
    """ checks for double letters """
    temp1 = ""
    for y in string:
        temp2 = y
        if temp1 == temp2:
            return True
        temp1 = temp2
    return False


def coals(string):
    """ checks for coal letter combinations """
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False
    return True


def twice(string):
    """ checks for pairs that appear twice"""
    temp1 = ""
    double_list = []
    for i, letter in enumerate(string):
        temp2 = letter
        double_list.append((temp1 + temp2, i))
        for z in double_list:
            if z[0] == temp1 + temp2 and i > (z[1] + 1):
                return True
        temp1 = temp2
    return False


def betweens(string):
    """ checks for repeat letters with letter between """
    for y in range(len(string) - 2):
        if string[y] == string[y + 2]:
            return True
    return False


nice_counter = 0
nice_counter2 = 0
for index, x in enumerate(string_list):
    if vowels(x) and doubles(x) and coals(x):
        nice_counter += 1
    if twice(x) and betweens(x):
        nice_counter2 += 1

print("Answer 1:", nice_counter)
print("Answer 2:", nice_counter2)
