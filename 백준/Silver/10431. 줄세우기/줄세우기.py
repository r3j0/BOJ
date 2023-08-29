import sys
input = sys.stdin.readline

p = int(input().rstrip())
for _ in range(p):
    t, *arr = map(int, input().rstrip().split())

    stack = []
    back = []

    cnt = 0
    for a in arr:
        if stack and max(stack) <= a:
            stack.append(a)
        else:
            while stack and max(stack) > a:
                now = stack.pop()
                back.append(now)
                cnt += 1

            stack.append(a)
            while back:
                now = back.pop()
                stack.append(now)
    
    print(t, cnt)