n = int(input())
a, b, c = map(int, input().split())
result = 0
if a > n: result += n
else: result += a
if b > n: result += n
else: result += b
if c > n: result += n
else: result += c
print(result)    