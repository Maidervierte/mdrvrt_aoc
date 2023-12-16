""" 2022 aoc07 """
with open("input07.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


class Node():
    """node"""
    def __init__(self, is_dir, name, parent, children, size):
        self.is_dir, self.name, self.parent, self.children, self.size = is_dir, name, parent, children, size


files = []
cur_node = Node(True, "/", Node(False, "None", "None", [], 0), [], 0)
counter = len(input_list)
files.append(cur_node)

for line in input_list[2:]:
    if "$" in line and "cd" in line and line.split(" ")[2] == "..":
        cur_node = cur_node.parent
    elif "$" in line and "cd" in line and line.split(" ")[2] == "/":
        cur_node = files[0]
    elif "$" in line and "cd" in line:
        for node in cur_node.children:
            if node.name == line.split(" ")[2]:
                cur_node = node
            if node.name == line.split(" ")[2]:
                break
    if "$" in line:
        continue
    if "dir" in line:
        temp_node = Node(True, line.split(" ")[1], cur_node, [], 0)
    else:
        temp_node = Node(False, line.split(" ")[1], cur_node, [], int(line.split(" ")[0]))
    cur_node.children, files = cur_node.children + [temp_node], files + [temp_node]
while counter != 0:
    counter = 0
    for file in files:
        if file.size == 0:
            counter += 1
        skip, size = True, 0
        for child in file.children:
            if child.size == 0:
                skip = True
            if child.size == 0:
                break
            size, skip = size + child.size, False
        if skip:
            continue
        file.size = size
needed_size, big_enough, remove_size = 30000000 - (70000000 - files[0].size), {}, 0
for file in files:
    if file.is_dir and file.size <= 100000:
        remove_size += file.size
    if file.is_dir and file.size >= needed_size:
        big_enough[file.size] = file

print("Answer 1:", remove_size)
print("Answer 2:", sorted(big_enough.items())[0][0])
