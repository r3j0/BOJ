# 35309 : 잘 정의된 들여쓰기
import sys
input = sys.stdin.readline
from collections import deque

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    s = deque()
    ans = 'YES'
    for a in arr:
        if a != 1: # 들여쓰기 번호가 1이 아니라면
            while s and s[-1] + 1 != a: # a와 연속된 번호가 나올때까지
                                        # 그동안 등장한 많게 들여쓰기한 브랜치들 지우기
                while s:
                    now = s.pop()
                    if now == 1:
                        break
            if not s: # 전부 다 비어버리면 NO
                ans = 'NO'
                break
        # 들여쓰기 번호가 1이거나, 연속된 번호를 발견했다면
        s.append(a)
    
    # 최종 점검, 들여쓰기 한 줄들이 잘 들여쓰기 되어있는지
    while s:
        # 들여쓰기 같은 줄들을 비운다.
        while s:
            now = s.pop()
            if now == 1:
                break
    if s: # 줄들이 남아있으면 NO
        ans = 'NO'

    print(ans)