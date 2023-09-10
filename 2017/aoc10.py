""" 2017 aoc10 """

with open("input10.txt", "r", encoding="utf-8") as f:
    input_string = f.read()

input_list = [int(x) for x in input_string.split(",")]
numbers = list(range(256))
cur_pos = 0
skip_size = 0
for length in input_list:
    new_numbers = []
    if cur_pos + length < len(numbers):
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
print("Answer 1:", numbers[0] * numbers[1])

ascii_list = []
for char in input_string:
    ascii_list.append(ord(char))
ascii_list += [17, 31, 73, 47, 23]
numbers = list(range(256))
cur_pos = 0
skip_size = 0
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

answer2 = ""
for value in hashed:
    if value > 16:
        answer2 += hex(value)[2:]
    else:
        answer2 += "0" + hex(value)[2:]

print("Answer 2:", answer2)
