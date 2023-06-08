result = []
while True:
    try:
        string = list(input().rstrip())
    except:
        break

    for s in range(len(string)):
        if string[s] == 'e': string[s] = 'i'
        elif string[s] == 'i': string[s] = 'e'
        elif string[s] == 'E': string[s] = 'I'
        elif string[s] == 'I': string[s] = 'E'
    
    result.append(string)

for r in result: print(''.join(map(str,r)))