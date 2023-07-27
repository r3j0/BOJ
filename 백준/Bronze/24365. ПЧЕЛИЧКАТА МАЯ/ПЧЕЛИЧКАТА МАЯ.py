a, b, c = map(int, input().split())
mid = (a+b+c)//3
midneed = 2 * mid - a
print(midneed - b + midneed - mid)