import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]
dic = {}

def backtracking(now, vis):
    global n
    global k
    global arr
    global dic
    if len(now) == k:
        now_s = ''.join(map(str, now))
        dic[now_s] = 1
        return
    
    for i in range(n):
        if vis[i] == 0:
            now.append(arr[i])
            vis[i] = 1
            backtracking(now, vis)
            vis[i] = 0
            now.pop()

backtracking([], [0 for _ in range(n)])
print(len(dic))