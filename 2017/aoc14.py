""" 2017 aoc14 """

with open("input14.txt", "r", encoding="utf-8") as f:
    input_word = f.read()

answer1 = 0
grid = []
for i in range(128):
    key_string = input_word + "-" + str(i)
    ascii_list = []
    cur_pos = 0
    skip_size = 0
    numbers = list(range(256))
    for char in key_string:
        ascii_list.append(ord(char))
    ascii_list += [17, 31, 73, 47, 23]
    for _ in range(64):
        for length in ascii_list:
            new_numbers = []
            if cur_pos + length <= len(numbers):
                new_numbers = numbers[:cur_pos] + \
                              list(reversed(numbers[cur_pos:cur_pos + length])) + \
                              numbers[cur_pos + length:]
            else:
                start_pos = (cur_pos + length) % len(numbers)
                to_reverse = list(reversed(numbers[cur_pos:] + numbers[:start_pos]))
                new_numbers = to_reverse[-start_pos:] + numbers[start_pos:cur_pos] + to_reverse[:-start_pos]
            numbers = new_numbers.copy()
            cur_pos += length + skip_size
            cur_pos = cur_pos % len(numbers)
            skip_size += 1

    hashed = []
    for x in range(16):
        xor = numbers[x * 16]
        for y in range(1, 16):
            xor ^= numbers[(x * 16) + y]
        hashed.append(xor)

    knot_hash = ""
    for value in hashed:
        if value >= 16:
            knot_hash += hex(value)[2:]
        else:
            knot_hash += "0" + hex(value)[2:]
    knot_hash_bin = ""
    for char in knot_hash:
        if int(char, 16) <= 1:
            knot_hash_bin += "000" + bin(int(char, 16))[2:]
        elif int(char, 16) <= 3:
            knot_hash_bin += "00" + bin(int(char, 16))[2:]
        elif int(char, 16) <= 7:
            knot_hash_bin += "0" + bin(int(char, 16))[2:]
        else:
            knot_hash_bin += bin(int(char, 16))[2:]

    grid.append(list(knot_hash_bin))
    answer1 += knot_hash_bin.count("1")

print("Answer 1:", answer1)

groups = 0
all_visited = set()
for x in range(128):
    for y in range(128):
        if grid[x][y] == "1" and (x, y) not in all_visited:
            groups += 1
            visited = set()
            visited.add((x, y))
            while len(visited) != 0:
                temp_visited = set()
                for (a, b) in visited:
                    if a > 0:
                        if grid[a - 1][b] == "1" and (a-1,b) not in all_visited:
                            temp_visited.add((a - 1, b))
                    if b > 0:
                        if grid[a][b - 1] == "1" and (a,b-1) not in all_visited:
                            temp_visited.add((a, b - 1))
                    if a < 127:
                        if grid[a + 1][b] == "1" and (a+1,b) not in all_visited:
                            temp_visited.add((a + 1, b))
                    if b < 127:
                        if grid[a][b + 1] == "1" and (a,b+1) not in all_visited:
                            temp_visited.add((a, b + 1))
                visited = temp_visited
                all_visited = all_visited.union(visited)
print("Answer 2:", groups)
