with open('input.txt') as file:
    lines = file.readlines()
    totalcount = 0
    counter = 0
    unique = []
    val = 0
    for i in range(len(lines[0])):
        uniqueL = True
        unique = []
        for n in range(i, i+14):
            
            if lines[0][n] in unique:
                uniqueL = False
            else:
                unique.append(lines[0][n])
                print(unique)
        
        if uniqueL == True:
            print(unique)
            print(i+14)
            break
