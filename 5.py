def id(line):
    binary = 0
    for char in line:
        if char == "F" or char == "L":
            binary = binary<<1
        else:
            binary = (binary<<1) + 1
    return binary

with open("input5") as input5:
    text = input5.read()
    m = id(text.split("\n")[0])
    for line in text.split("\n")[1:-1]:
        i = id(line)
        if i > m:
            m = i
    print(m)