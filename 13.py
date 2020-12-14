with open("input13") as input13:
    lines = input13.read().split("\n")[:-1]
    start = int(lines[0])
    buses = [int(x) for x in lines[1].split(",") if x != "x"]
    min_id = buses[0]
    min_time = 99999
    for bus in buses:
        trip = 0
        while trip < start:
            trip += bus
        wait = trip - start
        if wait < min_time:
            min_time = wait
            min_id = bus
    print(min_time * min_id)
