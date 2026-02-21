m, h = map(int, input().rstrip().split()) 
n = int(input().rstrip())
ans = 0
for i in range(n):
    a, b = map(int, input().rstrip().split())
    ans += max(m*a, h*b)
print(ans)