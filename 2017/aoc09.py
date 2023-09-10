""" 2017 aoc09 """

with open("input09.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

clean_text = ""
skip = False
for char in input_text:
    if skip:
        skip = False
        continue
    if char == "!":
        skip = True
        continue
    clean_text += char

depth = 0
score = 0
ignore = False
garbage = 0
for char in clean_text:
    if not ignore and char == "<":
        ignore = True
        continue
    if not ignore and char == "{":
        depth += 1
        score += depth
    if not ignore and char == "}":
        depth -= 1
    if ignore and char != ">":
        garbage += 1
    if ignore and char == ">":
        ignore = False
print("Answer 1:", score)
print("Answer 2:", garbage)
