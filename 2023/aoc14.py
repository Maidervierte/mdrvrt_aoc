""" 2023 aoc14 """

with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = [list(x) for x in f.read().splitlines()]


def tilt(_line):
    """tilts a single line"""
    _line = list(_line)
    for _i in range(len(_line) - 1, -1, -1):
        if _line[_i] == "O":
            cur_pos = _i
            while _i + 1 < len(_line) and _line[_i + 1] == ".":
                _i += 1
            if _i < len(_line) and _line[_i] == ".":
                _line[_i] = "O"
                _line[cur_pos] = "."
    return tuple(_line)


def north(_input_list):
    """tilts platform north"""
    _input_list = [list(x) for x in _input_list]
    for _j in range(len(_input_list[0])):
        _line = []
        for _i in range(len(_input_list) - 1, -1, -1):
            _line.append(_input_list[_i][_j])
        _line = list(tilt(tuple(_line)))
        for _i in range(len(_line)):
            _input_list[_i][_j] = _line[len(_line) - _i - 1]
    return tuple(tuple(x) for x in _input_list)


def west(_input_list):
    """tilts platform west"""
    _input_list = [list(x) for x in _input_list]
    for _i in range(len(_input_list)):
        _input_list[_i] = list(tilt(tuple(_input_list[_i][::-1])))[::-1]
    return tuple(tuple(x) for x in _input_list)


def south(_input_list):
    """tilts platform south"""
    _input_list = [list(x) for x in _input_list]
    for _j in range(len(_input_list[0])):
        line = []
        for _i in _input_list:
            line.append(_i[_j])
        line = list(tilt(tuple(line)))
        for _i, _char in enumerate(line):
            _input_list[_i][_j] = _char
    return tuple(tuple(x) for x in _input_list)


def east(_input_list):
    """tilts platform east"""
    _input_list = [list(x) for x in _input_list]
    for _i in range(len(_input_list)):
        _input_list[_i] = list(tilt(tuple(_input_list[_i])))
    return tuple(tuple(x) for x in _input_list)


def iteration(_input_list):
    """tilts platforms once in every direction"""
    _input_list = north(_input_list)
    _input_list = west(_input_list)
    _input_list = south(_input_list)
    _input_list = east(_input_list)
    return _input_list


input_list = tuple(tuple(x) for x in input_list)
input_list = north(input_list)

answer1 = 0
for i, _line in enumerate(input_list):
    for j, char in enumerate(_line):
        if char == "O":
            answer1 += len(input_list) - i
print("Answer 1:", answer1)

with open("input14.txt", "r", encoding="utf-8") as f:
    input_list = [list(x) for x in f.read().splitlines()]

i = 0
a_list = []
input_list = tuple(tuple(x) for x in input_list)
c_length = 0
while i < 1000000000:
    input_list = iteration(input_list)
    cur_answer = 0
    for index, line in enumerate(input_list):
        for char in line:
            if char == "O":
                cur_answer += len(input_list) - index
    a_list.append(cur_answer)
    for c in range(10, len(a_list)):
        for c_start in range(len(a_list)):
            if c_length == 0 and c_start + c + c < len(a_list):
                if a_list[c_start:c_start + c] == a_list[c_start + c:c_start + c + c]:
                    c_length = c
    if c_length != 0:
        new_counter = (1000000000 - i) // c_length
        i += new_counter * c_length + 1
    else:
        i += 1

answer2 = 0
for i, _line in enumerate(input_list):
    for j, char in enumerate(_line):
        if char == "O":
            answer2 += len(input_list) - i
print("Answer 2:", answer2)
