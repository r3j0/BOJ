import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

now = 0
cnt = 0
done = 0
for a in arr:
    now += a
    cnt += 1

    if now > t: 
        done = 1
        break

print(cnt - (1 if done == 1 else 0))