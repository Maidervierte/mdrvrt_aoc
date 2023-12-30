""" 2023 aoc23 """
import sys

with open("input23.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

trails = {}
for i, line in enumerate(input_list):
    for j, char in enumerate(line):
        trails[i, j] = char

hikes = [[(0, 1)]]
while hikes:
    temp = []
    for hike in hikes:
        x, y = hike[-1]
        match trails[x, y]:
            case "v":
                if (x + 1, y) not in hike:
                    temp.append(hike + [(x + 1, y)])
            case ">":
                if (x, y + 1) not in hike:
                    temp.append(hike + [(x, y + 1)])
            case _:
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (i, j) in trails and trails[i, j] != "#" and (i, j) not in hike:
                        temp.append(hike + [(i, j)])
    hikes = temp

print("Answer 1:", len(hike) - 1)


def next_node(cur_path, last_split, split_len):
    """gets next node"""
    _x, _y = cur_path[-1]
    next_nodes = []
    for _i, _j in [(_x + 1, _y), (_x - 1, _y), (_x, _y + 1), (_x, _y - 1)]:
        if (_i, _j) in trails and trails[_i, _j] != "#" and (_i, _j) not in cur_path:
            next_nodes.append(cur_path + [(_i, _j)])
    if len(next_nodes) > 1 or \
            (len(next_nodes) == 1 and next_nodes[0][-1] == (len(input_list) - 1, len(input_list[0]) - 2)):
        if next_nodes[0][-1] == (len(input_list) - 1, len(input_list[0]) - 2):
            split_len += 1000
        if last_split in new_trails and \
                (_x, _y, split_len) in new_trails[last_split] and \
                (_x, _y) in new_trails and \
                (*last_split, split_len) in new_trails[(_x, _y)]:
            return
        if last_split not in new_trails:
            new_trails[last_split] = set()
        if (_x, _y) not in new_trails:
            new_trails[_x, _y] = set()
        new_trails[last_split].add((_x, _y, split_len))
        new_trails[_x, _y].add((*last_split, split_len))
        for _n in next_nodes:
            next_node(_n, (_x, _y), 1)
    elif len(next_nodes) == 1:
        next_node(next_nodes[0], last_split, split_len + 1)


new_trails = {}
sys.setrecursionlimit(10000)
next_node([(0, 1)], (0, 1), 0)
queue = [(1, (0, 1))]
answer2 = 0
while queue:
    cur_path = queue.pop()
    for new_node in new_trails[cur_path[-1]]:
        if new_node[:2] not in cur_path:
            answer2 = max(answer2, cur_path[0] + new_node[2])
            new_path = (cur_path[0] + new_node[2],)
            new_path += cur_path[1:]
            new_path += ((new_node[0], new_node[1]),)
            queue.append(new_path)
    queue.sort()
print("Answer 2:", answer2 - 1000)

# while queue:
#     temp = []
#     for path in queue:
#         for new_node in new_trails[path[-1]]:
#             if new_node[:2] not in path:
#                 if (path[0] + new_node[2])>answer2:
#                     answer2 = max(answer2, path[0] + new_node[2])
#                     print(answer2)
#                 new_path = (path[0] + new_node[2],)
#                 new_path += path[1:]
#                 new_path += ((new_node[0], new_node[1]),)
#                 temp.append(new_path)
#     queue = temp.copy()
# print("Answer 2:",answer2)

# print("Answer 2:", answer2[0])
# """ 2023 aoc23 """
# from multiprocessing import Pool
#
#
# def new_hike(cur_hike):
#     """a"""
#     _new_hikes = []
#     _x, _y = cur_hike[-1]
#     for _i, _j in [(_x + 1, _y), (_x - 1, _y), (_x, _y + 1), (_x, _y - 1)]:
#         if (_i, _j) in trails and trails[_i, _j] != "#" and (_i, _j) not in cur_hike:
#             if finishable(cur_hike + [(_i, _j)]):
#                 _new_hikes.append(cur_hike + [(_i, _j)])
#     return _new_hikes
#
#
# def finishable(pos_hike):
#     """a"""
#     visited = set(pos_hike)
#     new_visited = set()
#     new_visited.add(pos_hike[-1])
#     possible = True
#     while possible:
#         possible = False
#         _temp = set()
#         for _x, _y in new_visited:
#             for _i, _j in [(_x + 1, _y), (_x - 1, _y), (_x, _y + 1), (_x, _y - 1)]:
#                 if (_i, _j) in trails and trails[_i, _j] != "#" and (_i, _j) not in visited:
#                     possible = True
#                     visited.add((_i, _j))
#                     _temp.add((_i, _j))
#         new_visited = _temp
#     if (len(input_list) - 1, len(input_list[0]) - 2) in visited:
#         return True
#     return False
#
#
# with open("input23.txt", "r", encoding="utf-8") as f:
#     input_list = f.read().splitlines()
#
# trails = {}
# for i, line in enumerate(input_list):
#     for j, char in enumerate(line):
#         trails[i, j] = char
#
# if __name__ == '__main__':
#     hikes = [[(0, 1)]]
#     while hikes:
#         temp = []
#         for hike in hikes:
#             x, y = hike[-1]
#             match trails[x, y]:
#                 case "v":
#                     if (x + 1, y) not in hike:
#                         temp.append(hike + [(x + 1, y)])
#                 case ">":
#                     if (x, y + 1) not in hike:
#                         temp.append(hike + [(x, y + 1)])
#                 case _:
#                     for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#                         if (i, j) in trails and trails[i, j] != "#" and (i, j) not in hike:
#                             temp.append(hike + [(i, j)])
#         hikes = temp
#
#     print("Answer 1:", len(hike) - 1)
#
#     finished_hike = []
#     hikes = [[(0, 1)]]
#
#     while hikes:
#         temp = []
#         with Pool(8) as p:
#             for new_hikes in p.map(new_hike, hikes):
#                 for hike in new_hikes:
#                     if (len(input_list) - 1, len(input_list[0]) - 2) in hike:
#                         finished_hike = hike
#                     temp.append(hike)
#         print(len(hike), len(hikes))
#         hikes = temp
#
#     print("Answer 2:", len(finished_hike) - 1)

#
# for i, line in enumerate(input_list):
#     for j, char in enumerate(line):
#         if (i, j) in finished_hike:
#             print("O", end="")
#         else:
#             print(char, end="")
#     print()

# """ 2023 aoc23 """
#
# with open("input23.txt", "r", encoding="utf-8") as f:
#     input_list = f.read().splitlines()
#
# trails = {}
# for i, line in enumerate(input_list):
#     for j, char in enumerate(line):
#         trails[i, j] = char
#
# hikes = [[(0, 1)]]
# while hikes:
#     temp = []
#     for hike in hikes:
#         x, y = hike[-1]
#         match trails[x, y]:
#             case "v":
#                 if (x + 1, y) not in hike:
#                     temp.append(hike + [(x + 1, y)])
#             case ">":
#                 if (x, y + 1) not in hike:
#                     temp.append(hike + [(x, y + 1)])
#             case _:
#                 for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#                     if (i, j) in trails and trails[i, j] != "#" and (i, j) not in hike:
#                         temp.append(hike + [(i, j)])
#     hikes = temp
#
# print("Answer 1:", len(hike) - 1)
#
# finished_hike=[]
# hikes = [[(0, 1)]]
# while hikes:
#     temp = []
#     for hike in hikes:
#         x, y = hike[-1]
#         for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#             if (i, j) in trails and trails[i, j] != "#" and (i, j) not in hike:
#                 temp.append(hike + [(i, j)])
#         if (len(input_list) - 1, len(input_list[0]) - 2) in hike:
#             finished_hike=hike
#     print(len(hike),len(hikes))
#     hikes = temp
#
# print("Answer 2:", len(finished_hike) - 1)
# #
# # for i, line in enumerate(input_list):
# #     for j, char in enumerate(line):
# #         if (i, j) in finished_hike:
# #             print("O", end="")
# #         else:
# #             print(char, end="")
# #     print()
