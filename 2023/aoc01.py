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

    calibration_value2 = ""
    cur = ""
    for char in line:
        if char.isdigit():
            calibration_value2 += char
            break
        cur += char
        if cur.replace("one", "1").replace("two", "2").replace("three", "3") \
                .replace("four", "4").replace("five", "5").replace("six", "6") \
                .replace("seven", "7").replace("eight", "8").replace("nine", "9") != cur:
            calibration_value2 += cur.replace("one", "1").replace("two", "2").replace("three", "3") \
                .replace("four", "4").replace("five", "5").replace("six", "6") \
                .replace("seven", "7").replace("eight", "8").replace("nine", "9")[-1]
            break

    cur = ""
    for char in reversed(line):
        if char.isdigit():
            calibration_value2 += char
            break
        cur = char + cur
        if cur.replace("one", "1").replace("two", "2").replace("three", "3") \
                .replace("four", "4").replace("five", "5").replace("six", "6") \
                .replace("seven", "7").replace("eight", "8").replace("nine", "9") != cur:
            calibration_value2 += cur.replace("one", "1").replace("two", "2").replace("three", "3") \
                .replace("four", "4").replace("five", "5").replace("six", "6") \
                .replace("seven", "7").replace("eight", "8").replace("nine", "9")[0]
            break

    answer1 += int(calibration_value)
    answer2 += int(calibration_value2)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
