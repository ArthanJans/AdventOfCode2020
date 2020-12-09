dic = {}
with open("input7") as input7:
    lines = input7.read().split("\n")[:-1]
    for line in lines:
        dic[line.split(" bags ")[0]] = " ".join(line.split(" bags ")[1:])

def totalinnerbags(name):
    line = dic[name]
    if line == "contain no other bags.":
        return 0
    else:
        bags = line.split("contain ")[1].split(", ")
        total = 0
        for bag in bags:
            n = int(bag.split(" ")[0])
            col = " ".join(bag.split(" ")[1:3])
            total += n * (totalinnerbags(col) + 1)
        return total
print(totalinnerbags("shiny gold"))
