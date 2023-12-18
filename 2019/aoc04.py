""" 2019 aoc04 """

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split("-")]

passwords = set()
for number in range(input_list[0], input_list[1] + 1):
    number = str(number)
    no_doubles = True
    skip = False
    for i, char in enumerate(number[:-1]):
        if char == number[i + 1]:
            no_doubles = False
        if int(char) > int(number[i + 1]):
            skip = True
            break
    if skip or no_doubles:
        continue
    passwords.add(number)
print("Answer 1:",len(passwords))

passwords = set()
for number in range(input_list[0], input_list[1] + 1):
    number = str(number)
    no_doubles = True
    skip = False
    for i, char in enumerate(number[:-1]):
        if char == number[i + 1]:
            if number.count(char) <= 2:
                no_doubles = False
        if int(char) > int(number[i + 1]):
            skip = True
            break
    if skip or no_doubles:
        continue
    passwords.add(number)
print("Answer 2:",len(passwords))
