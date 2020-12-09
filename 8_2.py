with open("input8") as input8:
    lines = input8.read().split("\n")[:-1]
    for index in range(len(lines)):
        copy = lines.copy()
        if copy[index][:3] == "nop":
            copy[index] = "jmp" + copy[index][3:]
        elif copy[index][:3] == "jmp":
            copy[index] = "nop" + copy[index][3:]
        acc = 0
        pc = 0
        run = {}
        while pc not in run:
            if pc == len(copy):
                print(acc)
                exit()
            line = copy[pc]
            op = line.split(" ")[0]
            num = int(line.split(" ")[1])
            run[pc] = True
            if op == "nop":
                pc += 1
                continue
            if op == "acc":
                acc += num
                pc += 1
                continue
            if op == "jmp":
                pc += num
                continue