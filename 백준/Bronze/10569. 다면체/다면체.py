n = int(input())
for _ in range(n):
    v, e = map(int, input().rstrip().split())
    print(2-v+e)