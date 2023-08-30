""" 2015 aoc07 """

with open("input07.txt", "r", encoding="utf-8") as f:
    instructions = f.read().splitlines()


def get_signal(gate):
    """ recursively calculates signal output"""
    if gate[0].isdigit():
        return int(gate)
    inp = input_dict[gate]
    if isinstance(inp, int):
        return inp
    if len(inp) == 1:
        input_dict[gate] = get_signal(inp[0])
    elif len(inp) == 2:
        input_dict[gate] = ~get_signal(inp[1])
    elif inp[1] == "AND":
        input_dict[gate] = get_signal(inp[0]) & get_signal(inp[2])
    elif inp[1] == "OR":
        input_dict[gate] = get_signal(inp[0]) | get_signal(inp[2])
    elif inp[1] == "RSHIFT":
        input_dict[gate] = get_signal(inp[0]) >> get_signal(inp[2])
    elif inp[1] == "LSHIFT":
        input_dict[gate] = get_signal(inp[0]) << get_signal(inp[2])
    return input_dict[gate]


input_dict = {}

for instruction in instructions:
    left_side, to_gate = instruction.split(" -> ")
    left_side = left_side.split(" ")
    input_dict[to_gate] = left_side

print("Answer 1: " + str(get_signal("a")))

for instruction in instructions:
    left_side, to_gate = instruction.split(" -> ")
    left_side = left_side.split(" ")
    if to_gate == "b":
        left_side = 3176
    input_dict[to_gate] = left_side

print("Answer 2: " + str(get_signal("a")))
