with open("input10") as input10:
    lines = input10.read().split("\n")[:-1]
    adapters = [int(x) for x in lines]
    adapters.sort()
    prev = 0
    diffs = []
    for adapter in adapters:
        diff = adapter - prev
        diffs.append(diff)
        prev = adapter
    diffs.append(3)
    consec = 0
    combos = 1
    consecs = []
    for diff in diffs:
        if diff == 1:
            consec += 1
        else:
            consecs.append(consec)
            consec = 0
    for consec in consecs:
        if consec == 2: # eg. 0 1 2 5 
            combos *= 2 # remove 1 or not remove 1
        if consec == 3: # eg. 0 1 2 3 6
            combos *= 4 # remove 1, 2, both, or none
        if consec == 4: # eg. 0 1 2 3 4 7
            combos *= 7 # remove 1, 2, 3, 1 2, 1 3, 2 3, or none
    print(combos)