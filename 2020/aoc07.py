""" 2020 aoc07 """

with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = [x.split(" contain ") for x in f.read().splitlines()]

bags = {}
for bag in input_list:
    bags[bag[0][:-5].replace("s", "")] = [
        (int(x[0]), x.replace(".", "").replace("s", "")[2:-4]) if x[0] != "n" else (0, "0")
        for x in bag[1].split(", ")]

cur_set = set()
cur_set.add("hiny gold")
cur_len = 0

while len(cur_set) != cur_len:
    cur_len = len(cur_set)
    for key, value in bags.items():
        for inside_bag in value:
            if inside_bag[1] in cur_set:
                cur_set.add(key)

print("Answer 1:", cur_len - 1)

answer2 = 0
new_bags = ["hiny gold"]
while new_bags:
    temp = []
    for new_bag in new_bags:
        inside_bags = bags[new_bag]
        for bag in inside_bags:
            answer2 += bag[0]
            for _ in range(bag[0]):
                temp.append(bag[1])
    new_bags = temp

print("Answer 2:", answer2)
