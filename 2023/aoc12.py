""" 2023 aoc12 """

from multiprocessing import Pool
from functools import cache

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()


@cache
def next_symbol(_nono, _key, cur_size):
    """handles the next symbol"""
    if len(_nono) == 0:
        if len(_key) == 0 and cur_size == 0:
            return 1
        if len(_key) == 1 and cur_size == _key[0]:
            return 1
        return 0

    if len(_key) > 0 and cur_size > _key[0]:
        return 0
    if len(_key) == 0 and cur_size > 0:
        return 0

    _answer = 0

    cur_symbol = _nono[0]

    match cur_symbol:
        case "#":
            _answer += next_symbol(_nono[1:], _key, cur_size + 1)
        case ".":
            if len(_key) > 0 and cur_size == _key[0]:
                _answer += next_symbol(_nono[1:], _key[1:], 0)
            elif cur_size == 0:
                _answer += next_symbol(_nono[1:], _key, 0)
        case "?":
            _answer += next_symbol(_nono[1:], _key, cur_size + 1)
            if len(_key) > 0 and cur_size == _key[0]:
                _answer += next_symbol(_nono[1:], _key[1:], 0)
            elif cur_size == 0:
                _answer += next_symbol(_nono[1:], _key, 0)

    return _answer


def solve1(line):
    """solves part 1"""
    nono = line.split(" ")[0]
    key = tuple(int(x) for x in line.split(" ")[1].split(","))
    answer = next_symbol(nono, key, 0)
    return answer


def solve2(line):
    """solves part 2"""
    nono = line.split(" ")[0]
    key = line.split(" ")[1]
    nono = nono + "?" + nono + "?" + nono + "?" + nono + "?" + nono
    key = tuple(int(x) for x in
                (key + "," + key + "," + key + "," + key + "," + key).split(","))
    answer = next_symbol(nono, key, 0)
    return answer


if __name__ == '__main__':
    with Pool(8) as p:
        print("Answer 1:", sum(p.map(solve1, input_list)))
        print("Answer 2:", sum(p.map(solve2, input_list)))
