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
                for area1 in range(index1-1, index1 + 2):
                    for area2 in range(index2-1, index2 + 2):
                        if area1 == index1 and area2 == index2:
                            continue
                        if area1 < 0 or area1 >= len(lines) or area2 < 0 or area2 >= len(lines[0]):
                            continue
                        if lines[area1][area2] == "#":
                            numoccupied += 1
                if lines[index1][index2] == "L" and numoccupied == 0:
                    newlines[index1][index2] = "#"
                if lines[index1][index2] == "#" and numoccupied >= 4:
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
                
