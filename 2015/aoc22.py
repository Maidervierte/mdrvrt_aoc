""" 2015 aoc22 """

import random

with open("input22.txt", "r", encoding="utf-8") as f:
    stat_lines = f.read().splitlines()

player_stats = {"hp": 50,
                "mana": 500,
                "magic missile": 0,
                "drain": 0,
                "shield": 0,
                "poison": 0,
                "recharge": 0}

boss_stats = {"hp": int(stat_lines[0].split(" ")[-1]),
              "dmg": int(stat_lines[1].split(" ")[-1])}

spells = {"magic missile": 53, "drain": 73, "shield": 113, "poison": 173, "recharge": 229}

lowest_mana_spent = 99999
attempt = 0
max_attempts = 100000000
while attempt < max_attempts/10:
    mana_spent = 0
    player = player_stats.copy()
    boss = boss_stats.copy()
    player_turn = True
    while True:
        if player_turn:
            if player["poison"] > 0:
                boss["hp"] -= 3
                player["poison"] -= 1
                if boss["hp"] <= 0:
                    won = True
                    break

            if player["shield"] > 0:
                player["shield"] -= 1

            if player["recharge"] > 0:
                player["mana"] += 101
                player["recharge"] -= 1

            if player["mana"] < 53:
                won = False
                break

            cur_spell = random.choice(sorted(spells))
            while player["mana"] < spells[cur_spell] or player[cur_spell] != 0:
                cur_spell = random.choice(sorted(spells))

            match cur_spell:
                case "magic missile":
                    boss["hp"] -= 4
                    player["mana"] -= 53
                    mana_spent += 53
                case "drain":
                    boss["hp"] -= 2
                    player["hp"] += 2
                    player["mana"] -= 73
                    mana_spent += 73
                case "shield":
                    player["mana"] -= 113
                    player["shield"] = 6
                    mana_spent += 113
                case "poison":
                    player["mana"] -= 173
                    player["poison"] = 6
                    mana_spent += 173
                case "recharge":
                    player["mana"] -= 229
                    player["recharge"] = 5
                    mana_spent += 229

            if boss["hp"] <= 0:
                won = True
                break
            player_turn = False
        else:
            if player["poison"] > 0:
                boss["hp"] -= 3
                player["poison"] -= 1
                if boss["hp"] <= 0:
                    won = True
                    break

            if player["recharge"] > 0:
                player["mana"] += 101
                player["recharge"] -= 1

            if player["shield"] > 0:
                player["hp"] = player["hp"] - max((boss["dmg"] - 7), 1)
                player["shield"] -= 1
            else:
                player["hp"] = player["hp"] - boss["dmg"]

            if player["hp"] <= 0:
                won = False
                break
            player_turn = True
    attempt += 1
    if won and mana_spent < lowest_mana_spent:
        lowest_mana_spent = mana_spent

print("Answer 1:", lowest_mana_spent)

lowest_mana_spent = 999999999
attempt = 0
while attempt < max_attempts:
    mana_spent = 0
    player = player_stats.copy()
    boss = boss_stats.copy()
    player_turn = True
    while True:
        if player_turn:
            player["hp"] -= 1
            if player["hp"] <= 0:
                won = False
                break

            if player["poison"] > 0:
                boss["hp"] -= 3
                player["poison"] -= 1
                if boss["hp"] <= 0:
                    won = True
                    break

            if player["shield"] > 0:
                player["shield"] -= 1

            if player["recharge"] > 0:
                player["mana"] += 101
                player["recharge"] -= 1

            if player["mana"] < 53:
                won = False
                break

            cur_spell = random.choice(sorted(spells))
            while player["mana"] < spells[cur_spell] or player[cur_spell] != 0:
                cur_spell = random.choice(sorted(spells))

            match cur_spell:
                case "magic missile":
                    boss["hp"] -= 4
                    player["mana"] -= 53
                    mana_spent += 53
                case "drain":
                    boss["hp"] -= 2
                    player["hp"] += 2
                    player["mana"] -= 73
                    mana_spent += 73
                case "shield":
                    player["mana"] -= 113
                    player["shield"] = 6
                    mana_spent += 113
                case "poison":
                    player["mana"] -= 173
                    player["poison"] = 6
                    mana_spent += 173
                case "recharge":
                    player["mana"] -= 229
                    player["recharge"] = 5
                    mana_spent += 229

            if boss["hp"] <= 0:
                won = True
                break
            player_turn = False
        else:
            if player["poison"] > 0:
                boss["hp"] -= 3
                player["poison"] -= 1
                if boss["hp"] <= 0:
                    won = True
                    break

            if player["recharge"] > 0:
                player["mana"] += 101
                player["recharge"] -= 1

            if player["shield"] > 0:
                player["hp"] -= max((boss["dmg"] - 7), 1)
                player["shield"] -= 1
            else:
                player["hp"] -= boss["dmg"]

            if player["hp"] <= 0:
                won = False
                break
            player_turn = True
    attempt += 1
    if won and mana_spent < lowest_mana_spent:
        lowest_mana_spent = mana_spent

print("Answer 2:", lowest_mana_spent)
