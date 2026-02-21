n = int(input())
a = input()
b = input()
ans = 0
for i in range(n):
    f = ord(a[i]) - ord(b[i])
    if f < 0: f += 26
    s = ord(b[i]) - ord(a[i])
    if s < 0: s += 26
    ans += min(f, s)
print(ans)