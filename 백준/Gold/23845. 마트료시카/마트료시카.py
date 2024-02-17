import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 연속된 수열 지속 제거하기
arr = list(map(int, input().rstrip().split()))
now = {}
for a in arr:
    if not now.get(a): now[a] = 1
    else: now[a] += 1

now = list(now.items())
now.sort(key=lambda x:x[0])
for i in range(len(now)): now[i] = list(now[i])

result = 0
while len(now) != 0:
    cnt = 0
    for i in range(len(now)):
        if i != len(now) - 1 and now[i][0] + 1 == now[i+1][0]:
            if cnt > 0: cnt += 1
            else: cnt += 2
        else:
            if cnt == 0:
                result += now[i][0] * now[i][1]
                now[i][1] = 0
            else:
                go = now[i][0]
                now[i][1] -= 1
                idx = i - 1
                for k in range(cnt - 1): now[idx - k][1] -= 1
                result += go * cnt
                cnt = 0
    idx = 0
    while idx < len(now):
        if now[idx][1] == 0:
            del now[idx]
        else:
            idx += 1

print(result)