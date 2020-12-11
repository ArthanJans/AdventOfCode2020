with open("input11") as input11:
    lines = [list(x) for x in input11.read().split("\n")[:-1]]
    changing = True
    while changing == True:
        newlines = [x.copy() for x in lines]
        for index1 in range(len(lines)):
            for index2 in range(len(lines[0])):
                if lines[index1][index2] == ".":
                    continue
                numoccupied = 0
                for dir in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
                    new1 = index1 + dir[0]
                    new2 = index2 + dir[1]
                    while not (new1 < 0 or new1 >= len(lines) or new2 < 0 or new2 >= len(lines[0])) and lines[new1][new2] == ".":
                        new1 += dir[0]
                        new2 += dir[1]
                    if (new1 < 0 or new1 >= len(lines) or new2 < 0 or new2 >= len(lines[0])):
                        continue
                    if lines[new1][new2] == "#":
                        numoccupied += 1
                if lines[index1][index2] == "L" and numoccupied == 0:
                    newlines[index1][index2] = "#"
                if lines[index1][index2] == "#" and numoccupied >= 5:
                    newlines[index1][index2] = "L"
        if newlines == lines:
            changing = False
        lines = newlines
    numoccupied = 0
    for index1 in range(len(lines)):
        for index2 in range(len(lines[0])):
            if lines[index1][index2] == "#":
                numoccupied += 1
    print(numoccupied)
                
