stack = []
def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return

    for i in range(start, n):
        if arr[i] not in stack:
            stack.append(arr[i])
            dfs(i+1)
            stack.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
dfs(0)