import re
with open("input4") as input4:
    pssprts = input4.read().split("\n\n")
    total = 0
    for psprt in pssprts:
        if "byr:" not in psprt:
            continue
        if len(psprt.split("byr:")[1].split()[0]) != 4 or int(psprt.split("byr:")[1].split()[0]) < 1920 or int(psprt.split("byr:")[1].split()[0]) > 2002:
            continue
        if "iyr:" not in psprt:
            continue
        if len(psprt.split("iyr:")[1].split()[0]) != 4 or int(psprt.split("iyr:")[1].split()[0]) < 2010 or int(psprt.split("iyr:")[1].split()[0]) > 2020:
            continue
        if "eyr:" not in psprt:
            continue
        if len(psprt.split("eyr:")[1].split()[0]) != 4 or int(psprt.split("eyr:")[1].split()[0]) < 2020 or int(psprt.split("eyr:")[1].split()[0]) > 2030:
            continue
        if "hgt:" not in psprt:
            continue
        hgt = psprt.split("hgt:")[1].split()[0]
        if hgt[-2:] == "cm":
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                continue
        elif hgt[-2:] == "in":
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                continue
        else:
            continue
        if "hcl:" not in psprt:
            continue
        hcl = psprt.split("hcl:")[1].split()[0]
        hex = re.compile("[0-9a-f]{6}")
        if len(hcl) != 7 or hcl[0] != "#" or hex.fullmatch(hcl[1:]) == None:
            continue
        if "ecl:" not in psprt:
            continue
        ecl = psprt.split("ecl:")[1].split()[0]
        cols = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if ecl not in cols:
            continue
        if "pid:" not in psprt:
            continue
        pid = psprt.split("pid:")[1].split()[0]
        if len(pid) != 9 or not pid.isnumeric():
            continue
        total += 1
    print(total)