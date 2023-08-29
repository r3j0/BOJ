import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a, b = input().rstrip().split()

arr = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

idx = 0
now = ""
while idx < n and idx < m:
    now += a[idx]
    now += b[idx]
    idx += 1

if idx < n:
    now += a[idx:]
if idx < m:
    now += b[idx:]

lis = []
for i in now:
    lis.append(arr[ord(i) - ord('A')])
lens = len(lis)
while lens != 2:
    new_lis = []
    for i in range(len(lis) - 1):
        new_lis.append((lis[i] + lis[i+1]) % 10)
    lis = new_lis
    lens = len(lis)

print('%d%%'%int(''.join(map(str, lis))))