import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
group = []

now_col = 'A'
now_cnt = 0
for i in range(n):
    if now_col != string[i]:
        if i != 0:
            group.append([now_col, now_cnt])
        now_col = string[i]
        now_cnt = 1
    else:
        now_cnt += 1

group.append([now_col, now_cnt])

# 빨간색 옮기기 - 앞으로
res = 0
for i in range(1, len(group)):
    if group[i][0] == 'R':
        res += group[i][1]

# 빨간색 옮기기 - 뒤로
now = 0
for i in range(len(group) - 1):
    if group[i][0] == 'R':
        now += group[i][1]

res = min(res, now)

# 파란색 옮기기 - 앞으로
now = 0
for i in range(1, len(group)):
    if group[i][0] == 'B':
        now += group[i][1]

res = min(res, now)

# 파란색 옮기기 - 뒤로
now = 0
for i in range(len(group) - 1):
    if group[i][0] == 'B':
        now += group[i][1]

res = min(res, now)

print(res)