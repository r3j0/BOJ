import sys
input = sys.stdin.readline

dic = {}
def backtracking(now):
    global arr
    if len(now) == 4:
        gogo = []
        for a in now:
            gogo.append(a)
        mv = -1
        for i in range(4):
            gogogo = []
            for j in range(4):
                gogogo.append(gogo[(i+j)%4])
            if mv == -1: mv = int(''.join(map(str, gogogo)))
            else: mv = min(mv, int(''.join(map(str, gogogo))))
        dic[mv] = 1
        return
    
    for i in range(1, 10):
        now.append(i)
        backtracking(now)
        now.pop()
backtracking([])
lis = list(sorted(dic.keys()))
order = list(map(int, input().rstrip().split()))

min_value = -1
for i in range(4):
    go = []
    for j in range(4):
        go.append(order[(i+j)%4])
    if min_value == -1: min_value = int(''.join(map(str, go)))
    else: min_value = min(min_value, int(''.join(map(str, go))))

print(lis.index(min_value) + 1)