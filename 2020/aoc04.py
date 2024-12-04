""" 2020 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split("\n\n")


def valid(_fields):
    """determines whether all fields are valid"""
    for field in fields:
        cat, value = field.split(":")
        if cat == "byr" and (int(value) < 1920 or int(value) > 2002):
            return False
        if cat == "iyr" and (int(value) < 2010 or int(value) > 2020):
            return False
        if cat == "eyr" and (int(value) < 2020 or int(value) > 2030):
            return False
        if cat == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if cat == "hgt" and ((value[-1] != "n" and value[-1] != "m") or
                             (value[-1] == "n" and (int(value[:-2]) < 59 or int(value[:-2]) > 76)) or
                             (value[-1] == "m" and (int(value[:-2]) < 150 or int(value[:-2]) > 193))):
            return False
        if cat == "pid" and (len(value) != 9 or not value.isdigit()):
            return False
        if cat == "hcl" and (value[0] != "#" or len(value) != 7 or any(
                (not x in ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                 for x in value[1:]))):
            return False
    return True


answer1 = 0
answer2 = 0
for line in input_list:
    fields = line.replace("\n", " ").split(" ")
    if len(fields) == 8 or (len(fields) == 7 and all("cid" not in x for x in fields)):
        answer1 += 1
        if valid(fields):
            print(sorted([x for x in fields if "cid" not in x]))
            answer2 += 1

print("Answer 1:", answer1)
print("Answer 2:", answer2)
