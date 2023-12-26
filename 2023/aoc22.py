""" 2023 aoc22 """

with open("input22.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

wall = {}
bricks = {}

for i, line in enumerate(input_list):
    a, b, c = line.split("~")[0].split(",")
    x, y, z = line.split("~")[1].split(",")
    for j in range(int(a), int(x) + 1):
        for k in range(int(b), int(y) + 1):
            for l in range(int(c), int(z) + 1):
                wall[j, k, l] = i
                if i in bricks:
                    bricks[i].add((j, k, l))
                else:
                    bricks[i] = set()
                    bricks[i].add((j, k, l))

for _ in range(1000):
    for brick in bricks:
        can_fall = True
        for x, y, z in bricks[brick]:
            if z == 1:
                can_fall = False
                break
            if (x, y, z - 1) in wall and wall[x, y, z - 1] != brick:
                can_fall = False
        if can_fall:
            temp = set()
            for x, y, z in bricks[brick]:
                temp.add((x, y, z - 1))
                wall.pop((x, y, z))
            bricks[brick] = temp
            for x, y, z in bricks[brick]:
                wall[x, y, z] = brick


# for z in range(10, 0, -1):
#     for x in range(3):
#         printed = False
#         for y in range(3):
#             if (x, y, z) in wall:
#                 print(wall[x, y, z], end="")
#                 printed = True
#                 break
#         if not printed:
#             print(".", end="")
#     print()

# for z in range(10, -1, -1):
#     for y in range(3):
#         printed = False
#         for x in range(3):
#             if (x, y, z) in wall:
#                 print(wall[x, y, z], end="")
#                 printed = True
#                 break
#         if not printed:
#             print(".", end="")
#     print()

def is_load_bearing(support, to_check):
    """checks if another brick supports this one"""
    for _x, _y, _z in bricks[to_check]:
        if (_x, _y, _z - 1) in wall and wall[_x, _y, _z - 1] not in [support, to_check]:
            return False
    return True


answer1 = 0
for brick in bricks:
    load_bearing = False
    for x, y, z in bricks[brick]:
        if (x, y, z + 1) in wall and wall[x, y, z + 1] != brick:
            if is_load_bearing(brick, wall[x, y, z + 1]):
                load_bearing = True
                break
    if not load_bearing:
        answer1 += 1
print("Answer 1:", answer1)

# def cascade(fallen_bricks):
#     """cascades fallen bricks"""
#     for _brick in bricks:
#         _can_fall = True
#         for _x, _y, _z in bricks[_brick]:
#             if _z == 1:
#                 _can_fall = False
#                 break
#             if (_x, _y, _z - 1) in wall and wall[_x, _y, _z - 1] not in fallen_bricks and wall[
#                 _x, _y, _z - 1] != _brick:
#                 _can_fall = False
#         if _can_fall:
#             fallen_bricks.add(_brick)
#     return fallen_bricks
#
#
# answer2 = 0
# for brick in bricks:
#     to_fall = set()
#     for x, y, z in bricks[brick]:
#         if (x, y, z + 1) in wall and wall[x, y, z + 1] != brick:
#             if is_load_bearing(brick, wall[x, y, z + 1]):
#                 to_fall.add(wall[x, y, z + 1])
#     temp = set()
#     while True:
#         temp = cascade(to_fall)
#         if temp == to_fall:
#             break
#         to_fall = temp
#     print(brick, len(to_fall), to_fall)
#     answer2 += len(to_fall)
# print("Answer 2:", answer2)

answer2 = 0
for brick in bricks:
    bricks2 = bricks.copy()
    wall2 = wall.copy()
    fallen_bricks = set()
    for x, y, z in bricks[brick]:
        wall2.pop((x, y, z))
    bricks2.pop(brick)
    for _ in range(10000):
        check = len(fallen_bricks)
        for brick2 in bricks2:
            can_fall = True
            for x, y, z in bricks2[brick2]:
                if z == 1:
                    can_fall = False
                    break
                if (x, y, z - 1) in wall2 and wall2[x, y, z - 1] != brick2:
                    can_fall = False
            if can_fall:
                fallen_bricks.add(brick2)
                temp = set()
                for x, y, z in bricks2[brick2]:
                    temp.add((x, y, z - 1))
                    wall2.pop((x, y, z))
                bricks2[brick2] = temp
                for x, y, z in bricks2[brick2]:
                    wall2[x, y, z] = brick2
        if len(fallen_bricks) == check:
            break
    answer2 += len(fallen_bricks)
print("Answer 2:", answer2)
