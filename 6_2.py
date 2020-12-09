with open("input6") as input6:
    groups = input6.read().split("\n\n")
    total = 0
    for group in groups:
        s = set(group.split("\n")[0])
        for person in group.split("\n"):
            s = s.intersection(set(person))
        total += len(s)
    print(total)