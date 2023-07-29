n = int(input())
arr = list(map(float, input().split()))
now = 0
for a in arr: now += a*a*a

print(now**(1/3))
