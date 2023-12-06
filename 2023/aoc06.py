""" 2023 aoc06 """

with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

times = [int(x) for x in input_list[0].split() if x.isdigit()]
distances = [int(x) for x in input_list[1].split() if x.isdigit()]
number_of_ways = []

for i, milliseconds in enumerate(times):
    goal_distance = distances[i]
    ways = 0
    for holding in range(milliseconds + 1):
        if holding * (milliseconds - holding) > goal_distance:
            ways += 1
    number_of_ways.append(ways)

print("Answer 1:", number_of_ways[0] * number_of_ways[1] * number_of_ways[2] * number_of_ways[3])

milliseconds = int("".join([str(x) for x in times]))
goal_distance = int("".join([str(x) for x in distances]))
ways = 0
for holding in range(milliseconds + 1):
    if holding * (milliseconds - holding) > goal_distance:
        ways += 1
print("Answer 2:", ways)
