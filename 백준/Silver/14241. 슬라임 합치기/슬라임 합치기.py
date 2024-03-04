import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
a = arr.pop()
b = arr.pop()
arr.append(a+b)
res = a * b
while len(arr) > 1:
    a = arr.pop()
    b = arr.pop()
    arr.append(a+b)
    res += a * b

print(res)

