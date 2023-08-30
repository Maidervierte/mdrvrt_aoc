""" 2015 aoc09 """

with open("input09.txt", "r", encoding="utf-8") as f:
    routes = f.read().splitlines()

# routes = "London to Dublin = 464\n" \
#          "London to Belfast = 518\n" \
#          "Dublin to Belfast = 141".splitlines()

distances = {}
city_set = set()
for route in routes:
    city1, _, city2, _, distance = route.split(" ")
    city_set.add(city1)
    city_set.add(city2)
    if city1 not in distances:
        distances[city1] = {}
    if city2 not in distances:
        distances[city2] = {}
    distances[city1][city2] = int(distance)
    distances[city2][city1] = int(distance)

possibles = []
for city in city_set:
    possibles.append([city])

possibles_dists = []
for possible in possibles:
    temp_dist = {}
    for key,value in distances.items():
        temp_dist[key] = dict(distances[key])
    while len(possible) < len(city_set):
        last_city = possible[-1]
        min_dist_city = min(temp_dist[last_city], key=temp_dist[last_city].get)
        if min_dist_city in possible:
            temp_dist[last_city].pop(min_dist_city)
        else:
            possible.append(min_dist_city)
    dist = 0
    for i in range(0, len(possible) - 1):
        dist += distances[possible[i]][possible[i + 1]]
    possibles_dists.append(dist)

print("Answer 1:" + str(min(possibles_dists)))

possibles = []
for city in city_set:
    possibles.append([city])

possibles_dists = []
for possible in possibles:
    temp_dist = {}
    for key,value in distances.items():
        temp_dist[key] = dict(distances[key])
    while len(possible) < len(city_set):
        last_city = possible[-1]
        min_dist_city = max(temp_dist[last_city], key=temp_dist[last_city].get)
        if min_dist_city in possible:
            temp_dist[last_city].pop(min_dist_city)
        else:
            possible.append(min_dist_city)
    dist = 0
    for i in range(0, len(possible) - 1):
        dist += distances[possible[i]][possible[i + 1]]
    possibles_dists.append(dist)

print("Answer 2:" + str(max(possibles_dists)))
