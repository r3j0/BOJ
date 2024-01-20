import sys
input = sys.stdin.readline

x = list(map(int, list(input().rstrip())))
cnt = 0
while len(x) != 1:
    allsum = sum(x)
    cnt += 1
    x = list(map(int, list(str(allsum))))

print(cnt)
print('YES' if x[0] in [3, 6, 9] else 'NO')