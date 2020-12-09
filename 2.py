with open("input2") as input2:
    lines = input2.read().split("\n")
    valid = 0
    for line in lines[:-1]:
        low = int(line.split("-")[0])
        high = int(line.split(" ")[0].split("-")[1])
        lett = line.split(":")[0].split(" ")[1]
        pw = line.split(": ")[1]
        count = pw.count(lett)
        if count <= high and count >= low:
            valid += 1
    print(valid)

