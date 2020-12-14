import math
with open("input12") as input12:
    lines = input12.read().split("\n")[:-1]
    pos = (0,0)
    waypoint = (10,1)
    angle = 0
    for line in lines:
        num = int(line[1:])
        char = line[0]
        if char == "N":
            waypoint = (waypoint[0],waypoint[1]+num)
        elif char == "E":
            waypoint = (waypoint[0]+num,waypoint[1])
        elif char == "S":
            waypoint = (waypoint[0],waypoint[1]-num)
        elif char == "W":
            waypoint = (waypoint[0]-num,waypoint[1])
        elif char == "R":
            if num == 90:
                waypoint = (waypoint[1], -waypoint[0])
            if num == 180:
                waypoint = (-waypoint[0], -waypoint[1])
            if num == 270:
                waypoint = (-waypoint[1], waypoint[0])
        elif char == "L":
            if num == 270:
                waypoint = (waypoint[1], -waypoint[0])
            if num == 180:
                waypoint = (-waypoint[0], -waypoint[1])
            if num == 90:
                waypoint = (-waypoint[1], waypoint[0])
        elif char == "F":
            pos = (pos[0] + waypoint[0] * num, pos[1] + waypoint[1] * num)
        print(waypoint)
        print(pos)

    print(pos)
    print(abs(pos[0]) + abs(pos[1]))