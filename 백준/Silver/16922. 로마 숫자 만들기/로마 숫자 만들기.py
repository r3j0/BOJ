import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = {}
def backtracking(now, arr, start):
    if now == n:
        go = 0
        for a in arr:
            if a == 'I': go += 1
            elif a == 'V': go += 5
            elif a == 'X': go += 10
            else: go += 50
        res[go] = 1
        return
    lis = ['I', 'V', 'X', 'L']
    for key in range(start, 4):
        arr.append(lis[key])
        backtracking(now+1, arr, key)
        arr.pop()


backtracking(0, [], 0)
print(len(res))