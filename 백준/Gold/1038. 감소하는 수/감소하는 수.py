import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = -1
arr = []
def backtracking(now):
    global n
    global result
    if len(now) > 0:
        done = True
        for i in range(1, len(now)):
            if now[i-1] <= now[i]:
                done = False
                break
        
        if done: 
            arr.append(int(''.join(map(str, now))))
        else:
            return
    
    for i in range(10):
        backtracking(now + [i])


backtracking([])
arr.sort()
if n < len(arr): print(arr[n])
else: print(-1)