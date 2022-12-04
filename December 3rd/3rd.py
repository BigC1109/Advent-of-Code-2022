with open('input.txt') as file:
    lines = file.readlines()
    totalList = []
    word1 = []
    word2 = []
    word3 = []
    counter = 0
    for line in lines:
        if counter == 0:
            for i in line.strip():
                word1.append(i)
            counter = 1
        elif counter == 1:
            for i in line.strip():
                word2.append(i)
            counter = 2
        elif counter == 2:
            for i in line.strip():
                word3.append(i)
            counter = 0
        
        
        if counter == 0:
            val = len(totalList)
            for i in word1:
                for k in word2:
                    for j in word3:
                        if i == k and i == j:
                            if val == len(totalList):
                                totalList.append(i)
            
            word1 = []
            word2 = []
            word3 = []
            counter = 0
                    
val = 0
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in totalList:
    print(i, alphabet.index(i) + 1)
    val += alphabet.index(i) + 1

print(val)