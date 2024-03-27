import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
vis = [0 for _ in range(n+1)]
res = []
for i in range(1, n+1):
    if vis[i] == 0:
        vis[i] = 1
        stack = []
        stack_vis = {}
        stack.append(i)
        stack_vis[i] = 1
        now = arr[i-1]
        while True:
            if stack_vis.get(now, -1) == -1:
                if vis[now] == 0:
                    vis[now] = 1
                    stack.append(now)
                    stack_vis[now] = 1
                    now = arr[now-1]
                else:
                    break
            else:
                goal = now
                while stack:
                    if stack[-1] == goal:
                        res.append(stack[-1])
                        stack.pop()
                        break
                    res.append(stack[-1])
                    stack.pop()
                break
res.sort()
print(len(res))
for r in res: print(r)