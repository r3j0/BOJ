import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []
for _ in range(n):
    arr = list(map(int, input().rstrip().split()))
    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        if len(stack) == 0: print(-1)
        else:
            print(stack[len(stack) - 1])
            del stack[len(stack) - 1]
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        if len(stack) == 0: print(1)
        else: print(0)
    elif arr[0] == 5:
        if len(stack) == 0: print(-1)
        else:
            print(stack[len(stack) - 1])