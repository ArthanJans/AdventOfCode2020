with open("input3") as input3:
    text = input3.read()
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    t = 1
    for slope in slopes:
        lines = text.split("\n")[:-1]
        pos = [0,0]
        total = 0
        while True:
            pos[0] += slope[0]
            pos[1] += slope[1]
            if pos[1] >= len(lines):
                break
            if pos[0] >= len(lines[0]):
                pos[0] -= len(lines[0])
            if lines[pos[1]][pos[0]] == "#":
                total += 1
        t *= total
    print(t)