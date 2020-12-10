with open("input10") as input10:
    lines = input10.read().split("\n")[:-1]
    adapters = [int(x) for x in lines]
    adapters.sort()
    ones = 0
    threes = 1
    prev = 0
    for adapter in adapters:
        if adapter - prev == 1:
            ones += 1
        if adapter - prev == 3:
            threes += 1
        prev = adapter
    print(threes * ones)
        