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

files = {}
i = 0
start_index = 0
file_id = 0
while i < len(input_list):
    files[start_index] = (file_id, input_list[i])
    file_id += 1
    start_index += input_list[i]
    i += 1
    if i < len(input_list):
        files[start_index] = (".", input_list[i])
        start_index += input_list[i]
        i += 1

for file_index in reversed(sorted(files.keys())):
    file_id, file_size = files[file_index]
    if file_id == ".":
        continue
    for space_index in sorted(files.keys()):
        if space_index >= file_index:
            break
        if files.get(space_index, [None])[0] != ".":
            continue
        space_size = files[space_index][1]
        if space_size == file_size:
            files[file_index] = (".", file_size)
            files[space_index] = (file_id, file_size)
            break
        if space_size > file_size:
            files[file_index] = (".", file_size)
            files[space_index] = (file_id, file_size)
            space_index += file_size
            files[space_index] = (".", space_size - file_size)
            break

answer2 = 0
start_index = 0
for file_index, (file_id, file_size) in files.items():
    if file_id == ".":
        continue
    for i in range(file_size):
        answer2 += (file_index + i) * file_id
print("Answer 2:", answer2)
