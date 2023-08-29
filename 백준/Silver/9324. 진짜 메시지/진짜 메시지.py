# 문자가 3번째로 등장하는 순간에 연달아 붙어있지 않다면 OK

import sys
input = sys.stdin.readline

t = int(input().rstrip()) 
for _ in range(t):
    string = input().rstrip()
    alpha = [0 for _ in range(26)]

    idx = 0
    done = 0
    while idx < len(string):
        alpha[ord(string[idx]) - ord('A')] += 1

        if alpha[ord(string[idx]) - ord('A')] % 3 == 0:
            if not (idx + 1 < len(string) and string[idx + 1] == string[idx]):
                done = 1
                break
            idx += 1
        idx += 1
    
    print('OK' if not done else 'FAKE')