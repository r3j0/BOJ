import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    string = input().rstrip()
    alpha = {chr(ord('A')+k):0 for k in range(26)}

    for s in string:
        if 'A' <= s <= 'Z':
            alpha[s] += 1
        elif 'a' <= s <= 'z':
            alpha[chr(ord(s) - 32)] += 1
    
    print('Case %d: '%i,end='')
    if min(list(alpha.values())) == 0: 
        print('Not a pangram')
    elif min(list(alpha.values())) == 1:
        print('Pangram!')
    elif min(list(alpha.values())) == 2:
        print('Double pangram!!')
    else:
        print('Triple pangram!!!')