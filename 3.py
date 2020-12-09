with open("input3") as input3:
    lines = input3.read().split("\n")[:-1]
    pos = [0,0]
    total = 0
    while pos[1] < len(lines) - 1:
        pos[0] += 3
        pos[1] += 1
        if pos[0] >= len(lines[0]):
            pos[0] -= len(lines[0])
        if lines[pos[1]][pos[0]] == "#":
            total += 1
    print(total)