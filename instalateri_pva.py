import math

def jeNaStene(bod, hrana):
    if ((bod[0] == 0 or bod[0] == hrana) and bod[1] >= 20 and bod[1] <= hrana-20 and bod[2] >= 20 and bod[2] <= hrana-20) or \
       ((bod[1] == 0 or bod[1] == hrana) and bod[0] >= 20 and bod[0] <= hrana-20 and bod[2] >= 20 and bod[2] <= hrana-20) or \
       ((bod[2] == 0 or bod[2] == hrana) and bod[1] >= 20 and bod[1] <= hrana-20 and bod[0] >= 20 and bod[0] <= hrana-20):
        return 1
    return 0

def minimum(seznam, pocet, chciIndex):
    minimum = seznam[0]
    min_in = 0
    for i in range(pocet):
        if seznam[i] < minimum:
            minimum = seznam[i]
            min_in = i
    return min_in if chciIndex else minimum

def minimumd(seznam, pocet, chciIndex):
    minimum = seznam[0]
    min_in = 0
    for i in range(pocet):
        if seznam[i] < minimum:
            minimum = seznam[i]
            min_in = i
    return min_in if chciIndex else minimum

hrana = int(input("Zadejte rozmer mistnosti:\n"))
if hrana < 0:
    print("Nespravny vstup.")
else:
    body = [[0, 0, 0], [0, 0, 0]]
    for i in range(2):
        print("Bod #{}:".format(i+1))
        bod = input().split()
        if len(bod) != 3 or not jeNaStene(list(map(int, bod)), hrana):
            print("Nespravny vstup.")
            exit()
        body[i] = list(map(int, bod))
    
    protejsi = 0
    potrubi = 0
    hadice = 0
    
    for i in range(3):
        if (body[0][i] == 0 and body[1][i] == hrana) or \
           (body[0][i] == hrana and body[1][i] == 0):
            protejsi = 1
            break
    
    stn = 0
    if protejsi:
        for i in range(3):
            if body[0][i] == hrana or body[0][i] == 0:
                stn = i
                break
        
        delky = [
            [
                hrana - body[0][1] + hrana + hrana - body[1][1], # nahoru
                hrana - body[0][2] + hrana + hrana - body[1][2], # doleva
                body[0][1] + hrana + body[1][1], # dolu
                body[0][2] + hrana + body[1][2] # doprava
            ],
            [
                abs(body[0][2] - body[1][2]), abs(body[0][1] - body[1][1]), abs(body[0][2]-body[1][2]), abs(body[0][1]-body[1][1])
            ]
        ]
        
        c = [delky[stn][0][0] + delky[stn][1][0], delky[stn][0][1] + delky[stn][1][1], delky[stn][0][2] + delky[stn][1][2], delky[stn][0][3] + delky[stn][1][3]]
        t = [
            math.sqrt(pow(delky[stn][0][0], 2.0) + pow(delky[stn][1][0], 2.0)),
            math.sqrt(pow(delky[stn][0][1], 2.0) + pow(delky[stn][1][1], 2.0)),
            math.sqrt(pow(delky[stn][0][2], 2.0) + pow(delky[stn][1][2], 2.0)),
            math.sqrt(pow(delky[stn][0][3], 2.0) + pow(delky[stn][1][3], 2.0))
        ]
        
        potrubi = minimum(c, 4, 0)
        hadice = minimumd(t, 4, 0)
    else:
        if body[0][0] != 0 and body[0][0] != hrana and body[1][0] != 0 and body[1][0] != hrana:
            hadice = math.sqrt((body[1][0] - body[0][0]) * (body[1][0] - body[0][0]) + (abs(body[1][1] - body[0][1]) + abs(body[1][2] - body[0][2])) * (abs(body[1][1] - body[0][1]) + abs(body[1][2] - body[0][2])))
        elif body[1][1] != 0 and body[1][1] != hrana and body[0][1] != 0 and body[0][1] != hrana:
            hadice = math.sqrt((body[1][1] - body[0][1]) * (body[1][1] - body[0][1]) + (abs(body[1][0] - body[0][0]) + abs(body[1][2] - body[0][2])) * (abs(body[1][0] - body[0][0]) + abs(body[1][2] - body[0][2])))
        elif body[1][2] != 0 and body[1][2] != hrana and body[0][2] != 0 and body[0][2] != hrana:
            hadice = math.sqrt((body[1][2] - body[0][2]) * (body[1][2] - body[0][2]) + (abs(body[1][0] - body[0][0]) + abs(body[1][1] - body[0][1])) * (abs(body[1][0] - body[0][0]) + abs(body[1][1] - body[0][1])))
        potrubi = abs(body[0][0] - body[1][0]) + abs(body[0][1] - body[1][1]) + abs(body[0][2] - body[1][2])
    
    print("Delka potrubi: {}\nDelka hadice: {}".format(potrubi, hadice))
