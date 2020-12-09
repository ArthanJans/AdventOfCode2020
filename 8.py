with open("input8") as input8:
    lines = input8.read().split("\n")[:-1]
    acc = 0
    pc = 0
    run = {}
    while pc not in run:
        line = lines[pc]
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
    print(acc)