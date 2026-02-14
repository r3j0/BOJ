t = int(input().rstrip())
for tc in range(t):
    a = list(map(int, input().rstrip().split()))
    a.sort()
    print('Case #%d: '%(tc+1) + ('YES' if a[0] ** 2 + a[1] ** 2 == a[2] ** 2 else 'NO'))