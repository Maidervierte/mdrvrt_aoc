""" 2017 aoc25 """
# with open("input25.txt", "r", encoding="utf-8") as f:
#     input_list = f.read().splitlines()
# fuck parsing that input

state = "A"
tape = {}
index = 0
for _ in range(12586542):
    match state:
        case "A":
            if index in tape:
                tape.pop(index)
                index -= 1
                state = "B"
            else:
                tape[index] = 1
                index += 1
                state = "B"
        case "B":
            if index in tape:
                index -= 1
                state = "B"
            else:
                index += 1
                state = "C"
        case "C":
            if index in tape:
                tape.pop(index)
                index -= 1
                state = "A"
            else:
                tape[index] = 1
                index += 1
                state = "D"
        case "D":
            if index in tape:
                index -= 1
                state = "F"
            else:
                tape[index] = 1
                index -= 1
                state = "E"
        case "E":
            if index in tape:
                tape.pop(index)
                index -= 1
                state = "D"
            else:
                tape[index] = 1
                index -= 1
                state = "A"
        case "F":
            if index in tape:
                index -= 1
                state = "E"
            else:
                tape[index] = 1
                index += 1
                state = "A"

print("Answer 1:", len(tape))
