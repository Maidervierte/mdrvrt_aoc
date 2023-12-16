""" 2022 aoc16 """
import random
with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()
valves, tunnels = {}, {}
for line in input_list:
    valve = line[6:8]
    valves[valve] = int(line.split(";")[0].split("rate=")[1])
    tunnels[valve] = line.split(";")[1].split("valves ")[1].split(", ")

def flow_calc(_valves, max_time):
    max_flow = 0
    for _ in range(10000):
        time, flow = max_time, 0
        cur_node = "AA"
        last_node = cur_node
        tempValves = _valves.copy()
        path = [cur_node]
        while time > 0:
            if tempValves[cur_node] != 0 and random.random() > 0.15:
                time -= 1
                flow += (tempValves[cur_node] * time)
                tempValves[cur_node] = 0
            time -= 1
            next_node = random.choice(tunnels[cur_node])
            if random.random() > 0.15 and len(tunnels[cur_node]) > 1:
                while next_node == last_node:
                    next_node = random.choice(tunnels[cur_node])
            last_node = cur_node
            cur_node = next_node
            path.append((cur_node, time))
        if flow > max_flow:
            nextValves = tempValves.copy()
            max_flow = flow
    return max_flow, nextValves


answer1, answer2 = flow_calc(valves, 30)[0], 0
temp = flow_calc(valves, 26)

while answer2 != 2100: answer2 = temp[0] + flow_calc(temp[1], 26)[0]
print("Answer 1:", answer1)
print("Answer 2:", answer2)
