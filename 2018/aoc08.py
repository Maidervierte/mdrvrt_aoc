""" 2018 aoc08 """

with open("input08.txt", "r", encoding="utf-8") as f:
    input_list = [int(x) for x in f.read().split(" ")]

INDEX = 0
ANSWER1 = 0
NODE_ID = 0
NODES = {}
padding = " "


def get_child_node():
    """gets... child node"""
    global INDEX, ANSWER1, NODE_ID, NODES, padding
    node_id = NODE_ID
    child_nodes = input_list[INDEX]
    INDEX += 1
    meta_nodes = input_list[INDEX]
    INDEX += 1
    children_ids = []
    for _ in range(child_nodes):
        NODE_ID += 1
        padding += " "
        children_ids.append(NODE_ID)
        get_child_node()
    meta_data = []
    for _ in range(meta_nodes):
        ANSWER1 += input_list[INDEX]
        meta_data.append(input_list[INDEX])
        INDEX += 1
    if child_nodes == 0:
        NODES[node_id] = sum(meta_data)
    else:
        node_value = 0
        for x in [y for y in meta_data if y <= len(children_ids)]:
            node_value += NODES[children_ids[x - 1]]
        NODES[node_id] = node_value
    padding = padding[:-1]


get_child_node()

print("Answer 1:", ANSWER1)
print("Answer 2:", NODES[0])
