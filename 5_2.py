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
    m = []
    for line in text.split("\n")[:-1]:
        i = id(line)
        m.append(i)
    m.sort()
    print(m)
    for index in range(1, len(m)):
        if m[index] != m[index - 1] + 1:
            print(m[index] - 1)
            exit()