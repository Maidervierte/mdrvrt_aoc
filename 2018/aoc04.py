""" 2018 aoc04 """
import datetime
import time

with open("input04.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

# input_list="[1518-11-01 00:00] Guard #10 begins shift\n" \
#            "[1518-11-01 00:05] falls asleep\n" \
#            "[1518-11-01 00:25] wakes up\n" \
#            "[1518-11-01 00:30] falls asleep\n" \
#            "[1518-11-01 00:55] wakes up\n" \
#            "[1518-11-01 23:58] Guard #99 begins shift\n" \
#            "[1518-11-02 00:40] falls asleep\n" \
#            "[1518-11-02 00:50] wakes up\n" \
#            "[1518-11-03 00:05] Guard #10 begins shift\n" \
#            "[1518-11-03 00:24] falls asleep\n" \
#            "[1518-11-03 00:29] wakes up\n" \
#            "[1518-11-04 00:02] Guard #99 begins shift\n" \
#            "[1518-11-04 00:36] falls asleep\n" \
#            "[1518-11-04 00:46] wakes up\n" \
#            "[1518-11-05 00:03] Guard #99 begins shift\n" \
#            "[1518-11-05 00:45] falls asleep\n" \
#            "[1518-11-05 00:55] wakes up".splitlines()
minutes = {}
for line in input_list:
    line_split = line.split(" ")
    month = int(line_split[0][6:8])
    day = int(line_split[0][9:])
    hour = int(line_split[1][:2])
    minute = int(line_split[1][3:-1])
    minutes[int(time.mktime(datetime.datetime(1970, month, day, hour, minute).timetuple()) // 60)] = line_split

guards = {}
guard = 2417
cur_guard = []
asleep = False
fell = 0
for key, value in list(sorted(minutes.items()))[1:]:
    match value[2]:
        case "Guard":
            guards[guard] = cur_guard
            guard = int(value[3][1:])
            if guard in guards:
                cur_guard = guards[guard]
            else:
                cur_guard = []
        case "falls":
            fell = key
            asleep = True
        case "wakes":
            for x in range(fell, key):
                cur_guard.append(x)
            asleep = False
max_sleep = 0
eepy_guard = 0
for guard, sleep in guards.items():
    if len(sleep) > max_sleep:
        max_sleep = len(sleep)
        eepy_guard = guard

minutes = []
for x in range(1440):
    minutes.append(0)

for minute in guards[eepy_guard]:
    dt = datetime.datetime.fromtimestamp(minute * 60)
    minutes[dt.hour * 60 + dt.minute] += 1

print("Answer 1:", eepy_guard * (minutes.index(max(minutes)) % 60))

max_asleep = 0
max_minute = 0
max_guard = 0
for guard, sleep in guards.items():
    minutes = []
    for x in range(1440):
        minutes.append(0)
    for minute in sleep:
        dt = datetime.datetime.fromtimestamp(minute * 60)
        minutes[dt.hour * 60 + dt.minute] += 1
        if max(minutes) > max_asleep:
            max_asleep = max(minutes)
            max_minute = minutes.index(max(minutes)) % 60
            max_guard = guard

print("Answer 2:", max_guard * max_minute)
