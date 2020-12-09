with open("input6") as input6:
    groups = input6.read().split("\n\n")
    total = 0
    for group in groups:
        total += len(set("".join(group.split("\n"))))
    print(total)