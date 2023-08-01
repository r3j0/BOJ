import sys
input = sys.stdin.readline

n = int(input().rstrip())
f = int(input().rstrip())

n = int(str(n)[:-2] + '00')
result = str(n)[-2:]
for i in range(100):
    if n % f == 0:
        result = str(n)[-2:]
        break
    n += 1

print(result)