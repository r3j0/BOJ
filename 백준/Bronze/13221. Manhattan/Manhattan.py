x, y = map(int, input().rstrip().split())
ans = []
t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    if ans == []: ans = [a, b]
    else:
        if abs(x - a) + abs(y - b) < abs(x - ans[0]) + abs(y - ans[1]):
            ans = [a, b]
print(' '.join(map(str, ans)))