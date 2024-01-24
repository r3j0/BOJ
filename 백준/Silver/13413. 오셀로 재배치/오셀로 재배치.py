import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    first = input().rstrip()
    second = input().rstrip()

    btow = 0
    wtob = 0

    for i in range(n):
        if first[i] == 'B' and second[i] == 'W': btow += 1
        elif first[i] == 'W' and second[i] == 'B': wtob += 1
    
    print(abs(btow-wtob) + min(btow, wtob))