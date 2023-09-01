""" 2015 aoc21 """

import random

with open("input21.txt", "r", encoding="utf-8") as f:
    stat_lines = f.read().splitlines()


def fight(_player, _boss):
    """ returns true if player wins """
    player = _player.copy()
    boss = _boss.copy()
    player_turn = True
    turn = 0
    while True:
        if player_turn:
            turn += 1
            # print("Turn:", turn)
            # print("  Player:", player)
            # print("  Boss", boss)
        if player_turn:
            boss["hp"] = boss["hp"] - max((player["dmg"] - boss["arm"]), 1)
            # print("    Player hits Boss for", max((player["dmg"] - boss["arm"]), 1), "damage!")
            if boss["hp"] <= 0:
                # print("### Player wins! ###")
                return True
            player_turn = False
        else:
            player["hp"] = player["hp"] - max((boss["dmg"] - player["arm"]), 1)
            # print("    Boss hits Player for", max((boss["dmg"] - player["arm"]), 1), "damage!")
            if player["hp"] <= 0:
                # print("### Boss wins! ###")
                return False
            player_turn = True


player_stats = {"hp": 100,
                "dmg": 0,
                "arm": 0}

boss_stats = {"hp": int(stat_lines[0].split(" ")[-1]),
              "dmg": int(stat_lines[1].split(" ")[-1]),
              "arm": int(stat_lines[2].split(" ")[-1])}

weapons = {8: 4, 10: 5, 25: 6, 40: 7, 74: 8}
armors = {13: 1, 31: 2, 53: 3, 75: 4, 102: 5}
rings = {25: "1d", 50: "2d", 100: "3d", 20: "1a", 40: "2a", 80: "3a"}

attempt = 0
lowest_cost = 74 + 102 + 100 + 80
while attempt < 10000:
    total_cost = 0
    weapon = random.choice(sorted(weapons))
    armor = 0
    if random.randint(0, 1) == 0:
        armor = random.choice(sorted(armors))
    cur_rings = random.sample(sorted(rings), random.randint(0, 2))
    cur_player_stats = player_stats.copy()
    cur_player_stats["dmg"] += weapons[weapon]
    total_cost += weapon
    total_cost += armor
    if armor != 0:
        cur_player_stats["arm"] += armors[armor]
    for ring in cur_rings:
        ring_stats = rings[ring]
        total_cost += ring
        if ring_stats[1] == "d":
            cur_player_stats["dmg"] += int(ring_stats[0])
        else:
            cur_player_stats["arm"] += int(ring_stats[0])
    if fight(cur_player_stats, boss_stats) and total_cost < lowest_cost:
        lowest_cost = total_cost
    attempt += 1

print("Answer 1:", lowest_cost)

attempt = 0
highest_cost = 0
while attempt < 10000:
    total_cost = 0
    weapon = random.choice(sorted(weapons))
    armor = 0
    if random.randint(0, 1) == 0:
        armor = random.choice(sorted(armors))
    cur_rings = random.sample(sorted(rings), random.randint(0, 2))
    cur_player_stats = player_stats.copy()
    cur_player_stats["dmg"] += weapons[weapon]
    total_cost += weapon
    total_cost += armor
    if armor != 0:
        cur_player_stats["arm"] += armors[armor]
    for ring in cur_rings:
        ring_stats = rings[ring]
        total_cost += ring
        if ring_stats[1] == "d":
            cur_player_stats["dmg"] += int(ring_stats[0])
        else:
            cur_player_stats["arm"] += int(ring_stats[0])
    if not fight(cur_player_stats, boss_stats) and total_cost > highest_cost:
        highest_cost = total_cost
    attempt += 1

print("Answer 2:", highest_cost)
