arr = [0 for _ in range(5)]
n = int(input())
for _ in range(n):
    a = int(input())
    arr[a-1] += 1

print('YES' if arr.count(0) > 0 else 'NO')