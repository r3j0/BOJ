n = int(input())
dic = {}
for _ in range(n):
    a = list(input().split())
    dic[int(a[1], 2)] = a[0]

s = input()
idx = 0
ans = ""
while idx < len(s):
    now = s[idx:idx+4]
    if dic.get(int(now, 2)):
        ans += dic[int(now, 2)]
    else:
        ans += "?"
    idx += 4
print(ans)