from math import prod
import time

with open("example13") as input13:
    lines = input13.read().split("\n")[:-1]
    tu = time.perf_counter()
    buses = lines[1].split(",")
    t = 1
    found=False
    done = []
    for index, bus in enumerate(buses):
        if bus == "x":
            continue
        while (t+index) % int(bus) != 0:
            t += prod(done)
        done.append(int(bus))
    print(t)
    print(time.perf_counter() - tu)