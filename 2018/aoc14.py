""" 2018 aoc14 """
with open("input14.txt", "r", encoding="utf-8") as f:
    input_number = f.read()

recipes = [3, 7]
elf1 = 0
elf2 = 1

while len(recipes) < (int(input_number) + 10):
    new_recipes = recipes[elf1] + recipes[elf2]
    for digit in str(new_recipes):
        recipes.append(int(digit))
    elf1 = (1 + elf1 + recipes[elf1]) % len(recipes)
    elf2 = (1 + elf2 + recipes[elf2]) % len(recipes)

print("Answer 1:", "".join([str(x) for x in recipes[int(input_number):int(input_number) + 10]]))

recipes = [3, 7]
elf1 = 0
elf2 = 1

while input_number not in "".join([str(x) for x in recipes[-10:]]):
    new_recipes = recipes[elf1] + recipes[elf2]
    for digit in str(new_recipes):
        recipes.append(int(digit))
    elf1 = (1 + elf1 + recipes[elf1]) % len(recipes)
    elf2 = (1 + elf2 + recipes[elf2]) % len(recipes)

print("Answer 2:", len(recipes) - len(input_number)-1)
