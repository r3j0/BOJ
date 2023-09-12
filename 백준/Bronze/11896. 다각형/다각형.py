a, b = map(int, input().rstrip().split())
a = max(3, a)
if a % 2 == 0: a -= 1
print(max(b//2*(b//2+1) - a//2*(a//2+1), 0))