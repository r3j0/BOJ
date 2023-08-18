import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
arr = [0 for _ in range(101)]
for _ in range(3):
    s, e = map(int, input().rstrip().split()) 
    for i in range(s, e):
        arr[i] += 1

res = 0
for i in range(101):
    if arr[i] == 3: res += c * 3        
    elif arr[i] == 2: res += b * 2
    elif arr[i] == 1: res += a

print(res)