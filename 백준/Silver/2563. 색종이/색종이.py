n = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
num = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                num += 1

print(num)