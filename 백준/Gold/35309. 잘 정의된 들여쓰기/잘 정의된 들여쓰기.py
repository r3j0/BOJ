# 35309 : 잘 정의된 들여쓰기
import sys
input = sys.stdin.readline
from collections import deque
"""
1
 1
 2
  1
 3
  1
  2
2
 1
 2
3

1 1 2 1 3 1 2 2 1 2 3
"""

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    s = deque()
    ans = 'YES'
    for a in arr:
        if not s:
            if a != 1:
                ans = 'NO'
                break
            s.append(a)
        else:
            if a != 1:
                while s and s[-1] + 1 != a:
                    while s:
                        now = s.pop()
                        if now == 1:
                            break
                if (not s) or (s[-1] + 1 != a):
                    ans = 'NO'
                    break
                s.append(a)
            else:
                s.append(a)
    print(ans)