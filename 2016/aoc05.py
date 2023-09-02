""" 2016 aoc05 """
import hashlib

with open("input05.txt", "r", encoding="utf-8") as f:
    input05 = f.read()
result = hashlib.md5(input05.encode()).hexdigest()

salt = -1
password = ""
for x in range(8):
    cur_hash = input05 + str(salt)
    result = hashlib.md5(cur_hash.encode()).hexdigest()
    while result[0:5] != "00000":
        cur_hash = input05 + str(salt)
        result = hashlib.md5(cur_hash.encode()).hexdigest()
        salt += 1
    password += result[5]

print("Answer 1:", password)

result = hashlib.md5(input05.encode()).hexdigest()

salt = -1
password = ["", "", "", "", "", "", "", ""]
while "" in password:
    cur_hash = input05 + str(salt)
    result = hashlib.md5(cur_hash.encode()).hexdigest()
    while result[0:5] != "00000":
        cur_hash = input05 + str(salt)
        result = hashlib.md5(cur_hash.encode()).hexdigest()
        salt += 1
        # print(result[0:5].count("0"), end="\r")
    if result[5] in ["0", "1", "2", "3", "4", "5", "6", "7"] and password[int(result[5])] == "":
        password[int(result[5])] = result[6]

print("Answer 2:", "".join(password))
