""" 2022 aoc03 """
with open("input03.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

prio_sum, prio_sum2 = 0, 0
for index in range(0, len(input_list) - 2, 3):
    a, b, c, d = str(set(input_list[index][:(len(input_list[index]) // 2)]).intersection(
        set(input_list[index][(len(input_list[index]) // 2):])))[2], \
        str(set(input_list[index + 1][:(len(input_list[index + 1]) // 2)]).intersection(
            set(input_list[index + 1][(len(input_list[index + 1]) // 2):])))[2], \
        str(set(input_list[index + 2][:(len(input_list[index + 2]) // 2)]).intersection(
            set(input_list[index + 2][(len(input_list[index + 2]) // 2):])))[2], \
        str(set(input_list[index]).intersection(set(input_list[index + 1])).intersection(input_list[index + 2]))[2]
    prio_sum, prio_sum2 = prio_sum + (ord(a) - 96 if ord(a) - 64 > 26 else ord(a) - 38) + (
        ord(b) - 96 if ord(b) - 64 > 26 else ord(b) - 38) + (
                              ord(c) - 96 if ord(c) - 64 > 26 else ord(c) - 38), prio_sum2 + (
                              ord(d) - 96 if ord(d) - 64 > 26 else ord(d) - 38)

print("Answer 1:", prio_sum)
print("Answer 2:", prio_sum2)
