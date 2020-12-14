import math
with open("input12") as input12:
    lines = input12.read().split("\n")[:-1]
    pos = (0,0)
    angle = 0
    for line in lines:
        num = int(line[1:])
        char = line[0]
        if char == "N":
            pos = (pos[0],pos[1]+num)
        elif char == "E":
            pos = (pos[0]+num,pos[1])
        elif char == "S":
            pos = (pos[0],pos[1]-num)
        elif char == "W":
            pos = (pos[0]-num,pos[1])
        elif char == "R":
            angle += num
            angle = angle % 360
        elif char == "L":
            angle -= num
            angle = angle % 360
        elif char == "F":
            ang = math.radians(angle)
            x = math.cos(ang) * num
            y = math.sin(ang) * num
            pos = (pos[0]+x,pos[1]-y)
    print(pos)
    print(abs(pos[0]) + abs(pos[1]))