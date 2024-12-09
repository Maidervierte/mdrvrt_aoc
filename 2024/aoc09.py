""" 2024 aoc09"""

with open("input09.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in list(f.read())]

files = []
file_id = 0
index = 0
i = 0
while i < len(input_list):
    file_size = input_list[i]
    for j in range(file_size):
        files.append(file_id)
    i += 1
    file_id += 1
    if i < len(input_list):
        free_space = input_list[i]
        for j in range(free_space):
            files.append(".")
        i += 1

temp = list(files)
for i, move_file in enumerate(reversed(temp)):
    if "." not in files:
        break
    files.pop(-1)
    if move_file == ".":
        continue
    files[files.index(".")] = move_file

answer1 = 0
for i, file_id in enumerate(files):
    answer1 += i * file_id
print("Answer 1:", answer1)

files = list(temp)
cur_sym = files[-1]
dots = 0
for i, move_file in enumerate(reversed(temp)):
    files_template = "".join(["x" if x != "." else "." for x in files])
    if "." not in files:
        break
    if move_file == ".":
        dots += 1
        continue
    if move_file != cur_sym:
        last_index = len(files) - list(reversed(files)).index(cur_sym)
        file_size = last_index - files.index(cur_sym)
        template = "." * file_size
        if template not in files_template:
            cur_sym = move_file
            dots = 0
            continue
        index = files_template.index(template)
        if index >= files.index(cur_sym):
            cur_sym = move_file
            dots = 0
            continue
        for j in range(index, index + len(template)):
            files[j] = cur_sym
            files[-i + j - index + dots] = "."
        cur_sym = move_file
    dots = 0

answer2 = 0
for i, file_id in enumerate(files):
    if file_id == ".":
        continue
    answer2 += i * file_id
print("Answer 2:", answer2)
