import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
dir = [60, 10, -10, 1, -1]

for _ in range(t):
    n = int(input().rstrip())
    start_arr = [n//60, 0, 0, 0, 0]
    n %= 60

    visited = [0 for _ in range(61)]
    visited[0] = 1
    queue = deque()
    queue.append([0, list(start_arr)])

    result = [0, 0, 0, 0, 0]
    done = False
    while queue:
        size = len(queue)
        for s in range(size):
            now_num, now_arr = queue.popleft()
            visited[now_num] = 1
            if now_num == n:
                if sum(result) == 0:
                    result = now_arr
                else:
                    for i in range(5):
                        if result[i] > now_arr[i]:
                            result = now_arr
                            break
                        elif result[i] < now_arr[i]:
                            break
            if done == False:
                for d in range(5):
                    if 0 < now_num + dir[d] < 61 and visited[now_num + dir[d]] == 0:
                        go_arr = list(now_arr)
                        go_arr[d] += 1
                        queue.append([now_num + dir[d], go_arr])
        
        if done == True: break
    
    print(' '.join(map(str, result)))