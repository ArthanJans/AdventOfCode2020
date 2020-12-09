with open("input2") as input2:
    lines = input2.read().split("\n")
    valid = 0
    for line in lines[:-1]:
        low = int(line.split("-")[0]) - 1
        high = int(line.split(" ")[0].split("-")[1]) - 1
        lett = line.split(":")[0].split(" ")[1]
        pw = line.split(": ")[1]
        if (pw[low] == lett or pw[high] == lett) and not (pw[low] == lett and pw[high] == lett):
            valid += 1
    print(valid)

