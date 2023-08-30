""" 2015 aoc04 """
import hashlib

with open("input04.txt", "r", encoding="utf-8") as f:
    input04 = f.read()

result = hashlib.md5(input04.encode()).hexdigest()

salt = -1
cur_hash = 0
while result[0:5] != "00000":
    salt += 1
    cur_hash = input04 + str(salt)
    result = hashlib.md5(cur_hash.encode()).hexdigest()

print("Answer 1:", cur_hash[len(input04):])

while result[0:6] != "000000":
    salt += 1
    cur_hash = input04 + str(salt)
    result = hashlib.md5(cur_hash.encode()).hexdigest()

print("Answer 2:", cur_hash[len(input04):])
