cratedict = {1: ['Z', 'P', 'M', 'H', 'R'],
2: ['P', 'C', 'J', 'B'],
3: ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
4: ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
5: ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
6: ['T', 'F', 'S', 'Z', 'B', 'G'],
7: ['N', 'R', 'V'],
8: ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
9: ['W', 'Q', 'N', 'J', 'F', 'M', 'L']}

with open('input.txt') as file:
    lines = file.readlines()

    for line in lines:
        newline = line.strip('movefromto').strip().split(' ')
        print(newline)
        
        index = len(cratedict[int(newline[2])]) - int(newline[0])
        print(index)
        for i in range(len(cratedict[int(newline[2])]), len(cratedict[int(newline[2])]) - int(newline[0]), -1):
            val = cratedict[int(newline[2])].pop(index)
            cratedict[int(newline[4])].append(val)

string = ''
for i in cratedict:
    string = string + cratedict[i][len(cratedict[i]) - 1]
print(string)
print(cratedict)