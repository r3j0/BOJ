import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = [0 for _ in range(10)]
if m != 0: 
    a = list(map(int, input().rstrip().split()))
    for i in a:
        arr[i] = 1
min_diff = -1

now = []
def backtracking():
    global min_diff

    if len(now) != 0:
        nint = int(''.join(map(str, now)))
        if min_diff == -1 or abs(n-min_diff) + len(str(min_diff)) > abs(n-nint) + len(str(nint)):
            min_diff = nint
    if len(now) == len(str(n)) + 1: return
    
    for i in range(10):
        if len(now) == 1 and now[-1] == 0: return
        if arr[i] == 1: continue

        now.append(i)
        backtracking()
        now.pop()

backtracking()

if min_diff != -1 and abs(n-100) > abs(n-min_diff) + len(str(min_diff)): print(abs(n-min_diff) + len(str(min_diff)))
else: print(abs(n-100))