""" 2020 aoc18"""
import re

with open("input18.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

answer1 = 0
answer2 = 0


def solve(expression):
    """solve"""
    expression = expression.split(" ")
    result = int(expression[0])
    _i = 1
    while _i < len(expression):
        match expression[_i]:
            case "*":
                result *= int(expression[_i + 1])
            case "+":
                result += int(expression[_i + 1])
        _i += 2
    return str(result)


def solve2(expression):
    """solve2"""
    while True:
        _search = re.search(r"\d+ \+ \d+", expression)
        if _search is None:
            break
        expression = expression[:_search.span()[0]] \
                     + solve(expression[_search.span()[0]:_search.span()[1]]) \
                     + expression[_search.span()[1]:]
    return solve(expression)


for i, line in enumerate(input_list):
    while True:
        search = re.search(r"\(\d+(?: [*+] \d+)+\)", line)
        if search is None:
            break
        line = line[:search.span()[0]] + \
               solve(line[search.span()[0]
                          + 1:search.span()[1] - 1]) \
               + line[search.span()[1]:]
    answer1 += int(solve(line))

for i, line in enumerate(input_list):
    while True:
        search = re.search(r"\(\d+(?: [*+] \d+)+\)", line)
        if search is None:
            break
        line = line[:search.span()[0]] \
               + solve2(line[search.span()[0] + 1:search.span()[1] - 1]) \
               + line[search.span()[1]:]
    answer2 += int(solve2(line))

print("Answer 1:", answer1)
print("Answer 2:", answer2)
