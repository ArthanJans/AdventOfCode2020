def mask(m, num):
    out = [0]
    offset = len(m) - len(num) + 2
    for index in range(0, len(m)):
        for i in range(len(out)):
            out[i] = out[i] << 1
        if m[index]=="0":
            if index < offset:
                continue
            if num[index-offset + 2] == "1":
                for i in range(len(out)):
                    out[i] = out[i] + 1
        if m[index]=="1":
            for i in range(len(out)):
                out[i] = out[i] + 1
        if m[index] == "X":
            change = out.copy()
            for i in range(len(out)):
                change[i] = change[i] + 1
            out = out + change
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
        for address in mask(currentmask, bin(adr)):
            mem[address] = num
    print(sum(mem.values()))