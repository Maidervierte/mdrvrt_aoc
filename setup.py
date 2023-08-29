import os

for year in range(2015, 2024):
    os.mkdir("./" + str(year) + "/")
    with open("./" + str(year) + "/.gitignore", "w+") as gitignore:
        gitignore.write("#inputs\n/input*")
    for day in range(1, 26):
        if day < 10:
            aoc_day = open("./" + str(year) + "/aoc0" + str(day)+".py", "w+")
            input_day = open("./" + str(year) + "/input0" + str(day)+".txt", "w+")
        else:
            aoc_day = open("./" + str(year) + "/aoc" + str(day)+".py", "w+")
            input_day = open("./" + str(year) + "/input0" + str(day)+".txt", "w+")
