""" 2015 aoc25 """
with open("input25.txt", "r", encoding="utf-8") as f:
    inputtext = f.read().split(" ")

row = int(inputtext[-3][:-1])
col = int(inputtext[-1][:-1])

code_num = 1
cur_row = 1
cur_col = 1
while cur_row != row or cur_col != col:
    cur_row -= 1
    cur_col += 1
    code_num += 1
    if cur_row < 1:
        cur_row = cur_col
        cur_col = 1

code = 20151125
for x in range(code_num - 1):
    code = (code * 252533) % 33554393
print("Answer 1:", code)
