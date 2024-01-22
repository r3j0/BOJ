import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
m = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

nowa = 0
for i in range(m-1, -1, -1):
    nowa += arr[i]*(a**(m-1-i))

new_arr = []
while nowa > 0:
    new_arr.append(nowa%b)
    nowa //= b

print(' '.join(map(str, new_arr[::-1])))