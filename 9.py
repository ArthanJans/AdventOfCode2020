with open("input9") as input9:
    lines = input9.read().split("\n")[:-1]
    for index in range(25, len(lines)):
        found = False
        for index2 in range(index-25, index):
            if not found:
                for index3 in range(index2, index):
                    if int(lines[index2]) + int(lines[index3]) == int(lines[index]):
                        found = True
                        break
        if not found:
            print(lines[index])
            exit()

