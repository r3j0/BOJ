import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []
now = []
res = 0
for i in range(1, n+1):
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 1:
        if len(now) > 0:
            stack.append(now)
        now = arr[1:]
        now[1] -= 1
        if now[1] == 0:
            res += now[0]
            if len(stack) > 0:
                now = stack.pop()
            else:
                now = [] 
    else:
        if len(now) > 0:
            now[1] -= 1
            if now[1] == 0:
                res += now[0]
                if len(stack) > 0:
                    now = stack.pop()
                else:
                    now = [] 
print(res)