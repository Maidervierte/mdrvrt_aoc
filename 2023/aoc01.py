""" 2023 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
for line in input_list:
    calibration_value = ""
    for char in line:
        if char.isdigit():
            calibration_value += char
            break
    for char in reversed(line):
        if char.isdigit():
            calibration_value += char
            break

    line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e") \
        .replace("four", "4").replace("five", "5e").replace("six", "6") \
        .replace("seven", "7n").replace("eight", "e8t").replace("nine", "n9e")
    calibration_value2 = ""
    for char in line:
        if char.isdigit():
            calibration_value2 += char
            break

    for char in reversed(line):
        if char.isdigit():
            calibration_value2 += char
            break

    answer1 += int(calibration_value)
    answer2 += int(calibration_value2)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
