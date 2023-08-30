""" 2015 aoc15 """
from itertools import combinations_with_replacement

with open("input15.txt", "r", encoding="utf-8") as f:
    ingredient_lines = f.read().splitlines()

ingredients = {}
for line in ingredient_lines:
    name, _, cap, _, dur, _, fla, _, tex, _, cal = line.split(" ")
    ingredients[name[:-1]] = {}
    ingredients[name[:-1]]["Cap"] = int(cap[:-1])
    ingredients[name[:-1]]["Dur"] = int(dur[:-1])
    ingredients[name[:-1]]["Fla"] = int(fla[:-1])
    ingredients[name[:-1]]["Tex"] = int(tex[:-1])
    ingredients[name[:-1]]["Cal"] = int(cal)

ingredients_set = set()
for key in ingredients.keys():
    ingredients_set.add(key)

recipes = list(combinations_with_replacement(ingredients_set, 100))
max_score = 0
max_score2 = 0
for recipe in recipes:
    for ingredient in ingredients.keys():
        ingredients[ingredient]["Amount"] = recipe.count(ingredient)
    scores = {}
    scores["Cap"] = 0
    scores["Dur"] = 0
    scores["Fla"] = 0
    scores["Tex"] = 0
    for ingredient, values in ingredients.items():
        scores["Cap"] += values["Amount"] * values["Cap"]
        scores["Dur"] += values["Amount"] * values["Dur"]
        scores["Fla"] += values["Amount"] * values["Fla"]
        scores["Tex"] += values["Amount"] * values["Tex"]
    for key, value in scores.items():
        if value < 0:
            scores[key] = 0
    score = 1
    for value in scores.values():
        score *= value
    scores["Cal"] = 0
    for ingredient, values in ingredients.items():
        scores["Cal"] += values["Amount"] * values["Cal"]
    if score > max_score:
        max_score = score
    if score > max_score2 and scores["Cal"] == 500:
        max_score2 = score

print("Answer 1:", max_score)
print("Answer 2:", max_score2)
