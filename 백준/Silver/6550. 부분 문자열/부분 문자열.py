import sys
input = sys.stdin.readline

while True:
    lis = ""
    try:
        lis = input().rstrip()
        if lis == "": break
    except:
        break

    s, t = lis.split()

    nows = 0
    for a in t:
        if nows < len(s) and a == s[nows]:
            nows += 1
    
    if len(s) == nows: print('Yes')
    else: print('No')