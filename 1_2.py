with open("input1") as input1:
    lines = input1.read().split("\n")
    for line in range(len(lines)-1):
        for line2 in range(line, len(lines)-1):
            for line3 in range(line2, len(lines)-1):
                if int(lines[line]) + int(lines[line2]) + int(lines[line3]) == 2020:
                    print(int(lines[line]) * int(lines[line2]) * int(lines[line3]))
                    exit()