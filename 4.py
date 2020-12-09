with open("input4") as input4:
    pssprts = input4.read().split("\n\n")
    total = 0
    for psprt in pssprts:
        if "byr:" not in psprt:
            continue
        if "iyr:" not in psprt:
            continue
        if "eyr:" not in psprt:
            continue
        if "hgt:" not in psprt:
            continue
        if "hcl:" not in psprt:
            continue
        if "ecl:" not in psprt:
            continue
        if "pid:" not in psprt:
            continue
        total += 1
    print(total)