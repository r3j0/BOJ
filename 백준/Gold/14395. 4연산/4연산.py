import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().rstrip().split())

if s == t: print(0)
elif s == 0: print(-1)
elif t == 0: print('-')
elif t == 1: print('/')
else:
    queue = deque()
    queue.append((s, 0, []))

    done = 0
    result_o = []
    while queue:
        now_s, now_g, now_o = queue.popleft()

        if now_s == t:
            done = 1
            result_o = now_o
            break

        if now_s == 0: continue
        
        if now_s != 1 and now_s * now_s <= t: queue.append((now_s * now_s, now_g, now_o + ['*']))
        if now_s + now_s <= t: queue.append((now_s + now_s, now_g, now_o + ['+']))
        if now_s != 1 and now_g == 0: queue.append((now_s // now_s, 1, now_o + ['/']))

    if done == 1: print(''.join(result_o))
    else: print(-1)