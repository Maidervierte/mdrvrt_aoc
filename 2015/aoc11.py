""" 2015 aoc11 """

with open("input11.txt", "r", encoding="utf-8") as f:
    password = f.read()


def increment_password(pw):
    """ increments password """
    for i in range(7, 0, -1):
        pw = pw[:i] + chr(ord(pw[i]) + 1) + pw[i + 1:]
        if ord(pw[i]) == 123:
            pw = pw[:i] + "a" + pw[i + 1:]
        else:
            break
    return pw


def check_password(pw):
    """ checks password validity """
    if "l" in pw or "i" in pw or "o" in pw:
        return False
    asc = False
    for i in range(5):
        if pw[i] != pw[i + 2] and \
                ord(pw[i]) < ord(pw[i + 2]) and \
                ((ord(pw[i]) + ord(pw[i + 2])) / 2) == ord(pw[i + 1]):
            asc = True
            break
    if not asc:
        return False
    i = 0
    doubles = 0
    while doubles < 2 and i < 7:
        if pw[i] == pw[i + 1]:
            doubles += 1
            i += 2
        else:
            i += 1
    if doubles < 2:
        return False
    return True


while not check_password(password):
    password = increment_password(password)
print("Answer 1: " + password)
password = increment_password(password)
while not check_password(password):
    password = increment_password(password)
print("Answer 2: " + password)
