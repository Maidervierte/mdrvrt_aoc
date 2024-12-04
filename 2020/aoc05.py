""" 2020 aoc05 """

with open("input05.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
seats = set(x for x in range(84, 902))
for line in input_list:
    row, seat = line[:7], line[7:]
    row = row.replace("B", "1").replace("F", "0")
    row = int(row, 2)
    seat = seat.replace("R", "1").replace("L", "0")
    seat = int(seat, 2)
    seats.remove(row * 8 + seat)
    answer1 = max(row * 8 + seat, answer1)
print("Answer 1:", answer1)
print("Answer 2:", seats.pop())
