""" 2017 aoc01 """

with open("input01.txt", "r", encoding="utf-8") as f:
    numberlist = f.read().strip()

temp = ""
captcha = 0
captcha2 = 0
for index, x in enumerate(numberlist):
    temp2 = numberlist[index - (int(len(numberlist) / 2))]
    if x == temp:
        captcha += int(temp)
    if x == temp2:
        captcha2 += int(temp2)
    temp = x

if numberlist[0] == temp:
    captcha += int(temp)
print("Answer 1:", captcha)
print("Answer 2:", captcha2)
