""" 2025 aoc02 """

with open("input02.txt", "r", encoding="utf-8") as f:
    input_list = [x.split("-") for x in f.read().split(",")]

answer1 = 0
answer2 = 0

for line in input_list:
    for x in range(int(line[0]),int(line[1])+1):
        if len(str(x))%2!=0:
            continue
        if str(x)[:len(str(x))//2]==str(x)[len(str(x))//2:]:
            answer1+=x


for line in input_list:
    found=set()
    for x in range(int(line[0]),int(line[1])+1):
        for i in range(1,len(str(x))//2+1):
            if x not in found and len(str(x))%i==0 and str(x).count(str(x)[:i])==len(str(x))//i:
                answer2+=x
                found.add(x)

print("Answer 1:", answer1)
print("Answer 2:", answer2)
