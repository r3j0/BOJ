import sys
input = sys.stdin.readline

n = int(input().rstrip())
status = [list(map(int, input().rstrip().split())) for _ in range(n)]

nv = 0
nv_avail = 0

def backtracking(now_team, start):
    global nv_avail
    global nv
    if len(now_team) * 2 == n:
        t1 = []
        t2 = []
        for i in range(n):
            if now_team.get(i, -1) == -1:
                t2.append(i)
            else:
                t1.append(i)
        t1s = 0
        t2s = 0
        for i in range(len(t1)):
            for j in range(len(t1)):
                t1s += status[t1[i]][t1[j]]
        for i in range(len(t2)):
            for j in range(len(t2)):
                t2s += status[t2[i]][t2[j]]
        
        if nv_avail == 0 or nv > abs(t1s-t2s):
            nv_avail = 1
            nv = abs(t1s-t2s)
        return

    for i in range(start, n):
        if now_team.get(i, -1) == -1:
            now_team[i] = 1
            backtracking(now_team, i + 1)
            del now_team[i]

backtracking({}, 0)
print(nv)