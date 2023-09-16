dic = {
    "1-1":"Habb Yakk", "2-2":"Dobara", "3-3":"Dousa", "4-4":"Dorgy", "5-5":"Dabash", "6-6":"Dosh",
    "1":"Yakk", "2":"Doh", "3":"Seh", "4":"Ghar", "5":"Bang", "6":"Sheesh"
}

import sys
input = sys.stdin.readline
t = int(input().rstrip())
for i in range(1,t+1):
    a, b = map(int, input().rstrip().split())
    if a == b: print('Case %d:'%i, dic[str(a)+"-"+str(b)])
    else:
        ma = str(max(a, b))
        mi = str(min(a, b))
        if ma == '6' and mi == '5': print('Case %d: Sheesh Beesh'%i)
        else:
            print('Case %d:'%i, dic[ma], dic[mi])