""" 2015 aoc12 """

with open("input12.txt", "r", encoding="utf-8") as f:
    json = f.read()

json = json.replace("\"", "")
summe = 0
cur_num = ""
for char in json:
    if char.isdigit() or char == "-":
        cur_num += char
    elif cur_num != "":
        summe += int(cur_num)
        cur_num = ""
print("Answer 1: " + str(summe))


def check_json():
    """ recursively calculates sum of object """
    global i
    l_sum = 0
    this_obj = ""
    while i < len(json):
        if json[i] == "{":
            i += 1
            l_sum += check_json()
        if json[i] == "}":
            i += 1
            break
        this_obj += json[i]
        i += 1
    if ":red" in this_obj:
        return 0
    l_cur_num = ""
    for l_char in this_obj:
        if l_char.isdigit() or l_char == "-":
            l_cur_num += l_char
        elif l_cur_num != "":
            l_sum += int(l_cur_num)
            l_cur_num = ""
    if l_cur_num != "":
        l_sum += int(l_cur_num)
    return l_sum


i = 1
print("Answer 2: " + str(check_json()))
