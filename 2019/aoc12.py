""" 2019 aoc12 """
import math

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = [[int(y[2:]) for y in x[1:-1].split(", ")] for x in f.read().splitlines()]

moons = {}
i = 0
for line in input_list:
    moons[i] = {"position": line, "velocity": [0, 0, 0]}
    i += 1


def update_velocity(cur_moon):
    """returns updated moon velocity"""
    pos = moons[cur_moon]["position"]
    vel = moons[cur_moon]["velocity"]
    for _moon, _values in moons.items():
        if cur_moon == _moon:
            continue
        for _i in range(3):
            if _values["position"][_i] > pos[_i]:
                vel[_i] += +1
            if _values["position"][_i] < pos[_i]:
                vel[_i] += -1
    return vel


def update_position(cur_moon):
    """returns updated moon position"""
    pos = moons[cur_moon]["position"]
    vel = moons[cur_moon]["velocity"]
    for _i in range(3):
        pos[_i] += vel[_i]
    return pos


for timestep in range(1000):
    for moon, values in moons.items():
        values["velocity"] = update_velocity(moon)
    for moon, values in moons.items():
        values["position"] = update_position(moon)

answer1 = 0
for moon,values in moons.items():
    pot = 0
    for position in values["position"]:
        pot += abs(position)
    kin = 0
    for velocity in values["velocity"]:
        kin += abs(velocity)
    answer1 += pot * kin
print("Answer 1:", answer1)

with open("input12.txt", "r", encoding="utf-8") as f:
    input_list = [[int(y[2:]) for y in x[1:-1].split(", ")] for x in f.read().splitlines()]

moons = {}
i = 0
for line in input_list:
    moons[i] = {"position": line, "velocity": [0, 0, 0]}
    i += 1

states_x = set()
states_y = set()
states_z = set()
for timestep in range(999999):
    state_x = ""
    state_y = ""
    state_z = ""
    for moon, values in moons.items():
        state_x += str(values["position"][0])
        state_x += str(values["velocity"][0])
        state_y += str(values["position"][1])
        state_y += str(values["velocity"][1])
        state_z += str(values["position"][2])
        state_z += str(values["velocity"][2])
    if state_x in states_x and state_y in states_y and state_z in states_z:
        break
    states_x.add(state_x)
    states_y.add(state_y)
    states_z.add(state_z)
    for moon, values in moons.items():
        values["velocity"] = update_velocity(moon)
    for moon, values in moons.items():
        values["position"] = update_position(moon)

print("Answer 2:", math.lcm(len(states_x), len(states_y), len(states_z)))
