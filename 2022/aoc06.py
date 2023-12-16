""" 2022 aoc06 """
with open("input06.txt", "r", encoding="utf-8") as f:
    input_list = f.read()

som1, som2 = False, False
for index, letter in enumerate(input_list):
    if len(set(input_list[index:index + 4])) == 4 and not som1:
        som1, answer1 = True, index + 3 + 1
    if len(set(input_list[index:index + 14])) == 14 and not som2:
        som2, answer2 = True, index + 13 + 1

print("Answer 1:", answer1)
print("Answer 2:", answer2)
