""" 2018 aoc11 """
with open("input11.txt", "r", encoding="utf-8") as f:
    input_number = int(f.read())

grid = {}

for x in range(1, 301):
    for y in range(1, 301):
        if x == 3 and y == 5:
            pass
        rack_id = x + 10
        power_level = rack_id * y
        power_level += input_number
        power_level *= rack_id
        if len(str(power_level)) < 3:
            grid[(x, y)] = -5
        else:
            grid[(x, y)] = int(str(power_level)[-3]) - 5

max_power_level = 0
answer1 = (0, 0)
for x in range(1, 299):
    for y in range(1, 299):
        cur_power_level = grid[(x, y)] + grid[(x, y + 1)] + grid[(x, y + 2)] \
                          + grid[(x + 1, y)] + grid[(x + 1, y + 1)] + grid[(x + 1, y + 2)] \
                          + grid[(x + 2, y)] + grid[(x + 2, y + 1)] + grid[(x + 2, y + 2)]
        if cur_power_level > max_power_level:
            max_power_level = cur_power_level
            answer1 = (x, y)

print("Answer 1:", answer1)

max_power_level = -450000
answer2 = (0, 0)
for size in range(1, 14):
    # t1 = time()
    for x in range(1, 302 - size):
        for y in range(1, 302 - size):
            cur_power_level = 0
            for _x in range(size):
                for _y in range(size):
                    cur_power_level += grid[(x + _x, y + _y)]
                    if cur_power_level < (max_power_level - ((size - _x) * (size - _y) * 9)):
                        break
            if cur_power_level > max_power_level:
                max_power_level = cur_power_level
                answer2 = (x, y, size)
    # print(size, answer2, max_power_level, time() - t1)

print("Answer 2:", answer2)

# grid = [[0 for x in range(300)] for y in range(300)]
#
# for x in range(0, 300):
#     for y in range(0, 300):
#         if x == 3 and y == 5:
#             pass
#         rack_id = x + 10
#         power_level = rack_id * y
#         power_level += input_number
#         power_level *= rack_id
#         if len(str(power_level)) < 3:
#             grid[x][y] = -5
#         else:
#             grid[x][y] = int(str(power_level)[-3]) - 5
#
# from time import time
# max_power_level = -450000
# answer1 = (0, 0)
# for size in range(299, -1, -1):
#     t1=time()
#     for x in range(0, 301 - size):
#         for y in range(0, 301 - size):
#             cur_power_level = 0
#             for _x in range(size):
#                 for _y in range(size):
#                     cur_power_level += grid[x + _x][y + _y]
#                     if cur_power_level < (max_power_level - ((size - _x) * (size - _y) * 9)):
#                         break
#             if cur_power_level > max_power_level:
#                 max_power_level = cur_power_level
#                 answer2 = (x+1, y+1, size)
#     print(size, max_power_level, time()-t1)
#
# print("Answer 2:", answer2)
