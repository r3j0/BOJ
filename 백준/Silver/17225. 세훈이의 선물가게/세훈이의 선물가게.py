import sys
input = sys.stdin.readline

a, b, n = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    t, c, m = input().rstrip().split()
    arr.append([int(t), c, int(m)])

arr.sort(key=lambda x:x[0])

sangmin_task = []
jisoo_task = []

sangmin_last = 0
jisoo_last = 0

sangmin_doing = -1
jisoo_doing = -1

sangmin_done = []
jisoo_done = []
cnt = 1

for time in range(0, 86401):
    if len(arr) > 0 and arr[0][0] == time:
        if arr[0][1] == 'B': sangmin_task.append(arr[0][2])
        else: jisoo_task.append(arr[0][2])
        del arr[0]

    if sangmin_last != 0: sangmin_last -= 1
    if sangmin_doing != -1 and sangmin_last == 0:
        sangmin_done.append(sangmin_doing)
        sangmin_doing = -1
    if jisoo_last != 0: jisoo_last -= 1  
    if jisoo_doing != -1 and jisoo_last == 0:
        jisoo_done.append(jisoo_doing)
        jisoo_doing = -1

    if a == 0:
        while sangmin_task:
            now = sangmin_task[0]
            for i in range(now):
                sangmin_done.append(cnt)
                cnt += 1
            del sangmin_task[0]
    else:
        if sangmin_doing == -1 and sangmin_last == 0 and len(sangmin_task) > 0:
            sangmin_task[0] -= 1
            sangmin_last = a

            sangmin_doing = cnt
            cnt += 1

            if sangmin_task[0] == 0:
                del sangmin_task[0]
    
    if b == 0:
        while jisoo_task:
            now = jisoo_task[0]
            for i in range(now):
                jisoo_done.append(cnt)
                cnt += 1
            del jisoo_task[0]
    else:
        if jisoo_doing == -1 and jisoo_last == 0 and len(jisoo_task) > 0:
            jisoo_task[0] -= 1
            jisoo_last = b

            jisoo_doing = cnt
            cnt += 1
            
            if jisoo_task[0] == 0:
                del jisoo_task[0]
    
        
print(len(sangmin_done))
print(' '.join(map(str, sangmin_done)))
print(len(jisoo_done))
print(' '.join(map(str, jisoo_done)))