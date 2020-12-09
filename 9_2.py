target = 1038347917
with open("input9") as input9:
    lines = [int(x) for x in input9.read().split("\n")[:-1]]
    found = False
    low=0
    high=1
    while not found:
        if sum(lines[low:high+1]) < target:
            high += 1
        elif sum(lines[low:high+1]) > target:
            low += 1
        else:
            print(min(lines[low:high+1]) + max(lines[low:high+1]))
            exit()
