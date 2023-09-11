import sys
input = sys.stdin.readline

L = int(input().rstrip())
R = int(input().rstrip())

arr = []
while True:
    L = int(L*R/100)
    if L <= 5: break
    arr.append(L)

sum_value = 0
for i in range(len(arr)):
    sum_value += (2**(i+1)) * arr[i]

print(sum_value)