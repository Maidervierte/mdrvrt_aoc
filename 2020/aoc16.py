""" 2020 aoc16"""

with open("input16.txt", "r", encoding="utf-8") as f:
    input_list = f.read().split("\n\n")

answer1 = 0
fields = []
my_ticket = [[int(y) for y in x.split(",")] for x in input_list[1].split("\n")[1:]][0]
nearby_tickets = [[int(y) for y in x.split(",")] for x in input_list[2].split("\n")[1:]]

rules = []
for line in input_list[0].splitlines():
    line = line.split(": ")
    fields.append(line[0])
    ranges = [list(range(int(x.split("-")[0]), int(x.split("-")[1]) + 1)) for x in line[1].split(" or ")]
    rules.append(ranges)

valid_tickets = []
for ticket in nearby_tickets:
    valid_ticket = True
    for value in ticket:
        valid = False
        for rule in rules:
            if value in rule[0] or value in rule[1]:
                valid = True
                break
        if not valid:
            valid_ticket = False
            answer1 += value
    if valid_ticket:
        valid_tickets.append(ticket)

ticket_fields = {}
answer2 = 1
allocated = set()
for i, field in enumerate(fields):
    value_ranges = rules[i]
    for j in range(len(fields)):
        valid_rule = True
        for ticket in valid_tickets:
            if ticket[j] not in value_ranges[0] and ticket[j] not in value_ranges[1]:
                valid_rule = False
                break
        if valid_rule:
            if field not in ticket_fields:
                ticket_fields[field] = [j]
            else:
                ticket_fields[field].append(j)

answer2 = 1
for _ in range(20):
    cur = []
    for field, fields in ticket_fields.items():
        if len(fields) == 1:
            cur.append((field, fields[0]))
    for name, field in cur:
        if "departure" in name:
            answer2 *= my_ticket[field]
        for fields in ticket_fields.keys():
            if field in ticket_fields[fields]:
                ticket_fields[fields].remove(field)
print("Answer 1:", answer1)
print("Answer 2:", answer2)
