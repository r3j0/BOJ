import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    alpha = {chr(k+ord('A')):0 for k in range(26)}
    for s in string:
        alpha[s] = 1
    
    result = 0
    for k in range(26):
        if alpha[chr(k+ord('A'))] == 0:
            result += k + 65
    
    print(result)