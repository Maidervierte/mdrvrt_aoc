""" 2019 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

# get all elements

elements = set()

for line in input_list:
    elements.add(line.split(")")[0])
    elements.add(line.split(")")[1])

# find element that doesnt orbit anything

no_orbit = set(elements)
for line in input_list:
    if line.split(")")[1] in no_orbit:
        no_orbit.remove(line.split(")")[1])

for element in no_orbit:
    no_orbit = element


def get_distance(cur_object, to_object):
    """returns distance between objects"""
    _distance = 0
    path = []
    while cur_object != to_object:
        for _line in input_list:
            if _line.split(")")[1] == cur_object:
                cur_object = _line.split(")")[0]
                _distance += 1
                path.append(_line.split(")")[0])
    return _distance, path


answer1 = 0

for element in elements:
    # print(element, get_distance(element, no_orbit))
    answer1 += get_distance(element, no_orbit)[0]
print("Answer 1: " + str(answer1))

you_path = get_distance("YOU", no_orbit)[1]
san_path = get_distance("SAN", no_orbit)[1]

while you_path[-1] == san_path[-1]:
    you_path.pop(-1)
    san_path.pop(-1)

print("Answer 1: " + str(len(you_path) + len(san_path)))
