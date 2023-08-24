n, m = map(int, input().rstrip().split())
cnt = 0
for _ in range(n):
    string = input()
    if string.count('+') > 0: cnt += 1
print(cnt)