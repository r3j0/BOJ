import sys
input = sys.stdin.readline

n, mode = input().rstrip().split()
n = int(n)

already = {}
ready = {}
cnt = 0

for _ in range(n):
    name = input().rstrip()
    if not already.get(name):
        already[name] = 1
        ready[name] = 1

        if (mode == 'Y' and len(ready) == 1) or (mode == 'F' and len(ready) == 2) or (mode == 'O' and len(ready) == 3):
            cnt += 1
            ready = {}

print(cnt)