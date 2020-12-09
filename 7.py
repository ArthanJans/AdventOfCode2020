with open("input7") as input7:
    lines = input7.read().split("\n")[:-1]
    found = {}
    nextfinding = []
    finding = ["shiny gold"]
    while finding != []:
        for line in lines:
            for find in finding:
                if find in " ".join(line.split(" bags ")[1:]) and line.split(" bags ")[0] not in found:
                    nextfinding.append(line.split(" bags ")[0])
                    found[line.split(" bags ")[0]] = True
        finding = nextfinding
        nextfinding = []
    print(len(found))