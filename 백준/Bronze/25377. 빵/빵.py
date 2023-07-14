n = int(input())
avail = []
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b: avail.append(b)
print(min(avail))