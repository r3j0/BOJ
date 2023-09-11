import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
result = []
for i in range(1, 5):
    arr.sort(key=lambda x:(-x[i], x[0]))
    result.append(arr[0][0])
    del arr[0]

print(' '.join(map(str, result)))