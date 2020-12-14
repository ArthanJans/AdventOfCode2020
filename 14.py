def mask(m, num):
    out = 0
    offset = len(m) - len(num) + 2
    for index in range(0, len(m)):
        out = out << 1
        if m[index]=="0":
            continue
        if m[index]=="1":
            out += 1
            continue
        if index < offset:
            continue
        if num[index-offset + 2] == "1":
            out += 1
    return out

with open("input14") as input14:
    lines = input14.read().split("\n")[:-1]
    currentmask = 0
    mem = {}
    for line in lines:
        if line.startswith("mask = "):
            currentmask = line.split(" = ")[1]
            continue
        adr = int(line.split("[")[1].split("]")[0])
        num = int(line.split(" = ")[1])
        mem[adr] = mask(currentmask, bin(num))
    print(sum(mem.values()))