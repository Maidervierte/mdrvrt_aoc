""" 2017 aoc18 """

with open("input18.txt", "r", encoding="utf-8") as f:
    input_list = f.read().splitlines()

a = 0
b = 0
f = 0
i = 0
p = 0

answer1 = 0
index = 0
recovered = False
while not recovered:
    line = input_list[index]
    ins = line.split(" ")[0]
    match ins:
        case "snd":
            exec("answer1=" + line.split(" ")[1])
            index += 1
        case "set":
            exec(line.split(" ")[1] + "=" + line.split(" ")[2])
            index += 1
        case "add":
            exec(line.split(" ")[1] + "+=" + line.split(" ")[2])
            index += 1
        case "mul":
            exec(line.split(" ")[1] + "*=" + line.split(" ")[2])
            index += 1
        case "mod":
            exec(line.split(" ")[1] + "%=" + line.split(" ")[2])
            index += 1
        case "rcv":
            exec("if " + line.split(" ")[1] + "!=0:print(\"Answer 1:\",answer1)")
            exec("if " + line.split(" ")[1] + "!=0:recovered=True")
            index += 1
        case "jgz":
            exec("if " + line.split(" ")[1] + ">0:index+=" + line.split(" ")[2])
            exec("if " + line.split(" ")[1] + "<=0:index+=1")
    index %= len(input_list)

cur_prog = 0
a1, b1, i1, f1, p1 = 0, 0, 0, 0, 0
a2, b2, i2, f2, p2 = 0, 0, 0, 0, 1
sending1 = []
index1 = 0
sending2 = []
index2 = 0
answer2 = 0
while (input_list[index1].split(" ")[0] != "rcv" or input_list[index2].split(" ")[0] != "rcv") or len(sending1) + len(
        sending2) != 0:
    if cur_prog == 0:
        line = input_list[index1]
        ins = line.split(" ")[0]
        match ins:
            case "snd":
                exec("sending1.append(" + line.split(" ")[1] + "1)")
                index1 += 1
            case "set":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "1=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "1=" + line.split(" ")[2] + "1")
                index1 += 1
            case "add":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "1+=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "1+=" + line.split(" ")[2] + "1")
                index1 += 1
            case "mul":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "1*=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "1*=" + line.split(" ")[2] + "1")
                index1 += 1
            case "mod":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "1%=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "1%=" + line.split(" ")[2] + "1")
                index1 += 1
            case "rcv":
                exec("if len(sending2)==0:cur_prog=1")
                exec("if len(sending2)!=0:index1+=1")
                exec("if len(sending2)!=0:" + line.split(" ")[1] + "1=sending2.pop(0)")
            case "jgz":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec("if " + line.split(" ")[1] + "1>0:index1+=" + line.split(" ")[2])
                else:
                    exec("if " + line.split(" ")[1] + "1>0:index1+=" + line.split(" ")[2] + "1")
                exec("if " + line.split(" ")[1] + "1<=0:index1+=1")
        index1 %= len(input_list)
    else:
        line = input_list[index2]
        ins = line.split(" ")[0]
        match ins:
            case "snd":
                exec("sending2.append(" + line.split(" ")[1] + "2)")
                index2 += 1
                answer2 += 1
            case "set":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "2=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "2=" + line.split(" ")[2] + "2")
                index2 += 1
            case "add":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "2+=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "2+=" + line.split(" ")[2] + "2")
                index2 += 1
            case "mul":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "2*=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "2*=" + line.split(" ")[2] + "2")
                index2 += 1
            case "mod":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec(line.split(" ")[1] + "2%=" + line.split(" ")[2])
                else:
                    exec(line.split(" ")[1] + "2%=" + line.split(" ")[2] + "2")
                index2 += 1
            case "rcv":
                exec("if len(sending1)==0:cur_prog=0")
                exec("if len(sending1)!=0:index2+=1")
                exec("if len(sending1)!=0:" + line.split(" ")[1] + "2=sending1.pop(0)")
            case "jgz":
                if line.split(" ")[2].lstrip("-").isdigit():
                    exec("if " + line.split(" ")[1] + "2>0:index2+=" + line.split(" ")[2])
                else:
                    exec("if " + line.split(" ")[1] + "2>0:index2+=" + line.split(" ")[2] + "2")
                exec("if " + line.split(" ")[1] + "2<=0:index2+=1")
        index2 %= len(input_list)

print("Answer 2:", answer2)
