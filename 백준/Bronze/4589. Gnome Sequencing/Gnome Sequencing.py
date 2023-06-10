t = int(input())
print('Gnomes:')
for _ in range(t):
    lis = list(map(int, input().split()))
    if lis == sorted(lis) or lis == sorted(lis, reverse=True): print('Ordered')
    else: print('Unordered')