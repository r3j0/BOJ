n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    arr.append((b*c*d, a, b+c+d))
arr.sort(key = lambda x:(x[0], x[2], x[1]))
print(arr[0][1], arr[1][1], arr[2][1])