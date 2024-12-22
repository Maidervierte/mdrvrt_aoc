""" 2024 aoc21"""
from itertools import permutations

with open("input21.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0
keypad1 = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
           "4": (1, 0), "5": (1, 1), "6": (1, 2),
           "1": (2, 0), "2": (2, 1), "3": (2, 2),
           "0": (3, 1), "A": (3, 2)}
keypad2 = {"^": (0, 1), "A": (0, 2),
           "<": (1, 0), "v": (1, 1), ">": (1, 2)}
dirs = {"^": (-1, 0), "v": (1, 0),
        "<": (0, -1), ">": (0, 1)}
sequences = {}


def sequence_length(code, max_keypad, cur_keypad):
    """sequence_length"""
    sequence = (code, max_keypad, cur_keypad)
    if sequence in sequences:
        return sequences[sequence]
    keypad = keypad1 if cur_keypad == 0 else keypad2
    x, y = keypad["A"]
    total = 0
    for char in code:
        i, j = keypad[char]
        to_move_x, to_move_y = ((i - x), (j - y))
        moves = []
        for _ in range(abs(to_move_x)):
            if to_move_x < 0:
                moves.append("^")
            else:
                moves.append("v")
        for _ in range(abs(to_move_y)):
            if to_move_y < 0:
                moves.append("<")
            else:
                moves.append(">")
        if moves:
            moves_list = set(permutations(moves))
            valid_moves_list = []
            for moves in moves_list:
                _x, _y = x, y
                for move in moves:
                    _i, _j = dirs[move]
                    _x, _y = ((_x + _i), (_y + _j))
                    if (_x, _y) not in keypad.values():
                        break
                else:
                    valid_moves_list.append("".join(moves + ("A",)))
        else:
            valid_moves_list = ["A"]
        min_len = 99999999999
        if cur_keypad == max_keypad:
            min_len = len(min(valid_moves_list, key=len))
            sequences[sequence] = min_len
            total += min_len
        else:
            for moves in valid_moves_list:
                cur_len = sequence_length(moves, max_keypad, cur_keypad + 1)
                min_len = min(cur_len, min_len)
            total += min_len
        x, y = i, j
    sequences[sequence] = total
    return total


for line in input_list:
    code_len = sequence_length(line, 2, 0)
    answer1 += code_len * int("".join([x for x in line if x.isdigit()]))
    code_len = sequence_length(line, 25, 0)
    answer2 += code_len * int("".join([x for x in line if x.isdigit()]))
print("Answer 1:", answer1)
print("Answer 2:", answer2)
