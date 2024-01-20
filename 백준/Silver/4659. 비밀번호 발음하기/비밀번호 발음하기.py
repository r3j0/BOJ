import sys
input = sys.stdin.readline

while True:
    x = list(input().rstrip())
    if ''.join(x) == 'end': break

    jaum = 0
    moum = 0
    moum_on = 0
    done = True
    for i in range(len(x)):
        if i == 0:
            if x[i] in ['a', 'e', 'i', 'o', 'u']: moum = 1
            else: jaum = 1
        else:
            if x[i] in ['a', 'e', 'i', 'o', 'u']: 
                if moum == 0:
                    moum = 1
                    jaum = 0
                else: moum += 1
            else: 
                if jaum == 0:
                    moum = 0
                    jaum = 1
                else: jaum += 1
            
            if moum == 3 or jaum == 3: 
                done = False
                break

            if x[i] == x[i-1] and (not ((x[i] == x[i-1] == 'e') or (x[i] == x[i-1] == 'o'))):
                done = False
                break

        if moum == 1: moum_on = 1
    
    if done == True and moum_on == 1: print('<%s> is acceptable.'%(''.join(x)))
    else: print('<%s> is not acceptable.'%(''.join(x)))