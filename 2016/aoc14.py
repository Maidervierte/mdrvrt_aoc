""" 2016 aoc14 """

import hashlib
import re

with open("input14.txt", "r", encoding="utf-8") as f:
    salt = f.read()

index = 0
keys = set()
while len(keys) < 64:
    hashed = hashlib.md5((salt + str(index)).encode("utf-8")).hexdigest()
    index += 1
    triples = re.findall(r'(.)\1\1', hashed)
    if len(triples) > 0:
        for i in range(1, 1001):
            _hashed = hashlib.md5((salt + str(index + i)).encode("utf-8")).hexdigest()
            if re.search("(" + triples[0] + r')\1\1\1\1', _hashed):
                keys.add(hashed)
print("Answer 1:", index - 1)

index = 0
keys = set()
pos_keys = []
for index in range(50000):
    hashed = hashlib.md5((salt + str(index)).encode("utf-8")).hexdigest()
    for _ in range(2016):
        hashed = hashlib.md5(hashed.encode("utf-8")).hexdigest()
    pos_keys.append(hashed)

stop = False
for i, pos_key in enumerate(pos_keys):
    triples = re.findall(r'(.)\1\1', pos_key)
    if len(triples) > 0:
        for j in range(1, 1001):
            if re.search("(" + triples[0] + r')\1\1\1\1', pos_keys[i + j]):
                keys.add(pos_key)
                if len(keys) == 64:
                    print("Answer 2:", i)
                    stop = True
                    break
    if stop:
        break
