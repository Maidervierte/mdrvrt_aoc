""" 2015 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    number_list = f.read().splitlines()


def paper_need(x, y, z):
    """ calculates needed paper """
    side1, side2, side3 = 2 * x * y, 2 * y * z, 2 * x * z
    return side1 + side2 + side3 + (min([side1, side2, side3]) / 2)


def ribbon_need(x, y, z):
    """ calculates needed ribbons """
    temp0 = [x, y, z]
    temp1 = min(temp0)
    temp2 = [x, y, z].index(temp1)
    temp0.pop(temp2)
    return min(x, y, z) * 2 + min(temp0) * 2 + x * y * z


square_feet = 0
ribbon = 0
for index, dim in enumerate(number_list):
    dimensions = dim.split("x")
    square_feet += paper_need(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
    ribbon += ribbon_need(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))

print("Answer 1:", square_feet)
print("Answer 2:", ribbon)
